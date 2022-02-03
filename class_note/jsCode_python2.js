
var p;
var c, d;

function setup(){
    size(800, 800)
    c= color(random(255), random(255), random(255))
    d= color(random(255), random(255), random(255))
}

function draw(){
for (var i=0; i=width, i++;){
p= lerpColor(c,d, 1.0*i/width)
stroke(p)
line(i, 0, i, height)
}

function mousePressed(){

c= color(random(255), random(255), random(255))
d= color(random(255), random(255), random(255))
}

}