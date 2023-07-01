import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  isElementVisible = true;

  toggleElements() {
    this.isElementVisible = !this.isElementVisible;
  }

  title = 'GUI';
}
