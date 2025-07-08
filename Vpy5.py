from vpython import *
from time import *

ballRadius = 1
wallThickness = 1
roomWidth = 5
roomDepth = 5
roomHeight = 5

floor1 = box(pos=vector(0,-roomHeight/2,0),color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
ceiling = box(pos=vector(0,roomHeight/2,0),color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
Rwall = box(pos=vector(roomWidth/2,0,0), color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
Lwall = box(pos=vector(-roomWidth/2,0,0),color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
Bwall = box(pos=vector(0,0,-roomDepth/2),color=color.white, size=vector(roomWidth,roomHeight,wallThickness))
ball = sphere(color=color.red, radius=ballRadius)
deltaX = 0.2
deltaY = 0.2
deltaZ = 0.2
xPos = 0
yPos = 0
zPos = 0

while True:
    rate(50)
    xPos+=deltaX
    yPos+=deltaY
    zPos+=deltaZ

    Xrme = xPos+ballRadius
    Xlme = xPos-ballRadius
    Rwe = (roomWidth/2)-(wallThickness/2)
    Lwe = -(roomWidth/2)+(wallThickness/2)

    Yume = yPos+ballRadius
    Ybme = yPos-ballRadius
    Cwe = (roomHeight/2)-(wallThickness/2)
    floorWe = -(roomHeight/2)+(wallThickness/2)

    Zfme = zPos+ballRadius
    Zbme = zPos-ballRadius
    Fwe = (roomDepth/2)-(wallThickness/2)
    Bwe = -(roomDepth/2)+(wallThickness/2)

    if Xrme>=Rwe or Xlme<=Lwe:
        deltaX*=-1
        ball.color = color.red
    if Yume>=Cwe or Ybme<=floorWe:
        deltaY*=-1
        ball.color = color.blue
    if Zfme>=Fwe or Zbme<=Bwe:
        deltaZ*=-1
        ball.color = color.green

    ball.pos=vector(xPos,yPos,zPos)