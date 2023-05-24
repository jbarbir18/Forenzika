import { Component } from '@angular/core';

@Component({
  selector: 'app-red-button',
  templateUrl: './red-button.component.html',
  styleUrls: ['./red-button.component.css']
})
export class RedButtonComponent {
  isButtonPushed = false;

  openPrompt(): void {
    this.isButtonPushed = true;
    

    // Delay to reset the pushed state after the animation completes
    setTimeout(() => {
      this.isButtonPushed = false;
      const confirmation = window.alert('Hi :)');
    }, 200);
    
  }
}
