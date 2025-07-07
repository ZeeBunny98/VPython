from vpython import *
from time import *

ballRadius = 0.75
wallThickness = 0.1
roomWidth = 15
roomDepth = 5
roomHeight = 10

floor1 = box(pos=vector(0,-roomHeight/2,0),color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
ceiling = box(pos=vector(0,roomHeight/2,0),color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
Rwall = box(pos=vector(roomWidth/2,0,0), color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
Lwall = box(pos=vector(-roomWidth/2,0,0),color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
Bwall = box(pos=vector(0,0,-roomDepth/2),color=color.white, size=vector(roomWidth,roomHeight,wallThickness))
ball = sphere(color=color.red, radius=ballRadius)
deltaX = 0.1
xPos = 0

while True:
    rate(50)
    xPos+=deltaX

    Xrme = xPos+ballRadius
    Xlme = xPos-ballRadius
    Rwe = (roomWidth/2)-(wallThickness/2)
    Lwe = -(roomWidth/2)+(wallThickness/2)

    if Xrme>=Rwe or Xlme<=Lwe:
        deltaX*=-1
    ball.pos=vector(xPos,0,0)