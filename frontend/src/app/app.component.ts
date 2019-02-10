import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


 @Component({
  selector: 'my-app',
  template: `<h1>bye {{name}}</h1>`,
})
    export class  AppComponent {
     name = "Hello2";

}


@Component({
  selector: 'my-app',
  template: `<h1>Hello {{name}}</h1>`,
})
export class AppComponent  { 
name = 'Angular'; 
}
