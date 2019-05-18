import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'dataGUI';
  videoNumber = "000000";
  videoname = this.videoNumber + '.mp4';
  leftRoundScore = "0";
  rightRoundScore = "0";
  leftScore = "0";
  rightScore = "0";
  winSide = "left";
  frame = "0";
  score = this.leftRoundScore + ' ' + this.rightRoundScore + ' '+ this.leftScore + ' ' + this.rightScore + ' '+this.winSide;

  lineAction = "";
  action = '';
  
  finalTxt = [];
  output = this.finalTxt.join("\n");
  changeWinSide(){
    if (this.winSide === 'left') {
      this.winSide = "right";
    }else{
      this.winSide = "left";
    }
    this.onKey(event);

  }
  onKey(event: any) { // without type info
    this.score = this.leftRoundScore + ' ' + this.rightRoundScore + ' '+ this.leftScore + ' ' + this.rightScore + ' '+this.winSide;
  }
  onKey1(event: any){
    this.lineAction = this.frame + ' ' + this.action;
  }

  changeAction(event){
    this.action = event.target.title
    this.onKey1(event);
    // this.lineAction = this.frame + ' ' + ;
  }

  addline1(){
    this.finalTxt.push(this.videoname);
    this.output = this.finalTxt.join("\n");

  }
  addline2(){
    this.finalTxt.push(this.score);
    this.output = this.finalTxt.join("\n");
    
  }
  addline3(){
    this.finalTxt.push(this.lineAction);
    this.output = this.finalTxt.join("\n");

  }

  delete() {
    this.finalTxt.pop();
    this.output = this.finalTxt.join("\n");
    
  }

  reset(){
    this.finalTxt = [];
    this.output = this.finalTxt.join("\n");

  }



}
