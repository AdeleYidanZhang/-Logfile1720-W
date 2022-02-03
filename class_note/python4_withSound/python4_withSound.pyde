add_library('sound')

c, d, ch_1, ch_2=None, None, None, None

def setup():
    size(800, 800)
    global c, d
    c= color(random(255), random(255), random(255))
    d= color(random(255), random(255), random(255))
    
    global ch_1, ch_2
    
    ch_1 = SinOsc(this)
    ch_1.play(0,1)
    ch_2 = SinOsc(this)
    ch_2.play(0,1)
    
    
def draw():
    background(255)
    stroke(0)
    noFill()
    constantFactor =1.315
    circleSize= 20
    
    global c, d
    global ch_1, ch_2
    
    if mousePressed:
    ch_1.set(400, 1, 0, 0)
    ch_2.set(400, 1, 0, 0)
        
    else:
    
  
    for i in range(width):
        p=lerpColor(c,d, 1.0*i/width)
        stroke(p)
        #line(i, 0, i, height)
        
        strokeWeight(circleSize/25.0)
         ellipse(width/2, height, circleSize, circleSize)
         circleSize = circleSize* constantFactor
        
def mousePressed():
    global c, d 
    c= color(random(255), random(255), random(255))
    d= color(random(255), random(255), random(255))
    ch_1 =
    ch_2 =
