from vpython import *
from time import *

floor1 = box(pos=vector(0,-5,0),color=color.white, size=vector(10,0.1,10))
ceiling = box(pos=vector(0,5,0),color=color.white, size=vector(10,0.1,10))
Rwall = box(pos=vector(5,0,0), color=color.white, size=vector(0.1,10,10))
Lwall = box(pos=vector(-5,0,0),color=color.white, size=vector(0.1,10,10))
Bwall = box(pos=vector(0,0,-5),color=color.white, size=vector(10,10,0.1))
ball = sphere(color=color.red, radius=0.75)
deltaX = 0.1
xPos = 0

while True:
    rate(30)
    xPos+=deltaX
    if xPos>(5-ball.radius-0.1) or xPos<(-5+ball.radius+0.1):
        deltaX*=-1
    ball.pos=vector(xPos,0,0)