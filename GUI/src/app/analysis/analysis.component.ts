import { Component, OnInit } from '@angular/core';
import { userData } from 'src/assets/userData';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-analysis',
  templateUrl: './analysis.component.html',
  styleUrls: ['./analysis.component.css']
})
export class AnalysisComponent implements OnInit {
  jsonData !: any;
  headers !: string[];

  userData !: userData;


  constructor(private http:HttpClient) { 
    this.headers = ["Key", "Value"];

  }

  ngOnInit() {
    this.http.get('./assets/data.txt', { responseType: 'text' })
      .subscribe(
        (response: string) => {
          const parsedData = JSON.parse(response);
          this.jsonData = parsedData; 
          this.userData = this.jsonData; 
          // Process the parsed data here
          console.log(this.jsonData);
        },
        (error: any) => {
          console.error('Error fetching JSON file:', error);
        }
      );
      
    
  }
}
