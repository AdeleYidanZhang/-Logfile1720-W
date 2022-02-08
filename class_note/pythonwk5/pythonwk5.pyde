#Rings:
    #A way to count the rings
    numRings = 40
    #A way to store rings
    ring =[0]*numRings
    #keep track of which rings
    currentRing = 0
    #to change ring color
    colour= None



def setup():
size(600, 600)
smooth()

global numRings, ring;

for i in range(numRings):
colour = color(random(255),random(255),random(255));
ring[i] = Ring(0, 0, 0, False, colour);#create each object

def draw():
global numRings, rings;

def mousePressed():
    #when we click we want to activate a ring ar the loction of the cursor
    #so our xpos=mouseX
    #ypos=mouseY
global numRings, rings;
    ring[currentRing].start(mouseX, mouseY);
    
    currentRing+=1;
    if(currentRing>= numRings):
        currentRing=0;
    
    
class Ring(Object):
       
#1. initialize
def _init_(self, x, y, diameter, on, colour):#positionX, positionY, drawing on/off, change colour; 
self.x=x;
self.y=y;
self.diameter = diameter;
self.on=False;
self.colour=colour;

#2.start
def start(self, xpos, ypos):
    self.x= xpos;
    self.y= ypos;
    self.on= True;
    self.diameter = 1;
#3.grow
def grow(self):
    if(self.on==True):
        self.diameter +=1.5;
        if(self.diameter>400):
            self.on= False
#4.display
def display(self):
    if(self.on==True):
        noFill()
        strokeWeight(4)
        stroke(self.colour)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
