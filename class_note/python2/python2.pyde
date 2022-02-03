c, d =None, None

def setup():
    size(800, 800)
    global c, d
    c= color(random(255), random(255), random(255))
    d= color(random(255), random(255), random(255))
    
def draw():
    global c, d
    for i in range(width):
        p=lerpColor(c,d, 1.0*i/width)
        stroke(p)
        line(i, 0, i, height)
    
def mousePressed():
    global c, d 
    c= color(random(255), random(255), random(255))
    d= color(random(255), random(255), random(255))
