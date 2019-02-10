import os
from flask import jsonify
from app import app
from flask import flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s/newdb.db' % os.getcwd()


db = SQLAlchemy(app)
ma = Marshmallow(app)

class Author(db.Model):
    __tablename__ = 'Authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', backref='books')

class AuthorSchema(ma.ModelSchema):
    class Meta:
        model = Author

@app.route('/api/users/')
def authors():
    all_authors = db.session.query(Author).all()
    result = author_schema.dump(all_authors)
    return jsonify(result)
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run(debug = True)