color bgColor=color(0);//black color
float circleSize=100;

void setup(){
  size(800, 600, P2D);// P2D enables 2D GPU acceleration
  ellipseMode(CENTER);
  background(bgColor);
}
  
  void draw(){
    println(mousePressed);
    if(mousePressed){
      fill(0,5);//could replace 0 to bgcolor
      rect(0, 0, width, height);
      //rectMode(CENTER);
      fill(0, 127, 255);
      stroke(255, 0, 0);
      //line(mouseX, mouseY, pmouseX, pmouseY);
      ellipse(mouseX, mouseY, 10, 10);
    }
  }
