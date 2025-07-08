from vpython import *
from time import *
import random

ballRadius = 0.5
wallThickness = 0.1
roomWidth = 20
roomDepth = 15
roomHeight = 15

floor1 = box(pos=vector(0,-roomHeight/2,0),color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
ceiling = box(pos=vector(0,roomHeight/2,0),color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
Rwall = box(pos=vector(roomWidth/2,0,0), color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
Lwall = box(pos=vector(-roomWidth/2,0,0),color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
Bwall = box(pos=vector(0,0,-roomDepth/2),color=color.white, size=vector(roomWidth,roomHeight,wallThickness))

ball1 = sphere(color=color.red,radius=ballRadius)
ball2 = sphere(color=color.blue,radius=ballRadius)
ball3 = sphere(color=color.green,radius=ballRadius)

deltaX = 0.1
deltaY = 0.1
deltaZ = 0.1

deltaX2 = 0.2
deltaY2 = 0.2
deltaZ2 = 0.2

deltaX3 = 0.3
deltaY3 = 0.3
deltaZ3 = 0.3

xPos = 0
yPos = 0
zPos = 0

xPos2 = 1
yPos2 = 1
zPos2 = 1

xPos3 = 2
yPos3 = 2
zPos3 = 2

while True:
    rate(50)
    #Ball 1
    xPos+=deltaX
    yPos+=deltaY
    zPos+=deltaZ
    #Ball 2
    xPos2+=deltaX2
    yPos2+=deltaY2
    zPos2+=deltaZ2
    #Ball 3
    xPos3+=deltaX3
    yPos3+=deltaY3
    zPos3+=deltaZ3

    #room
    Rwe = (roomWidth/2)-(wallThickness/2)
    Lwe = -(roomWidth/2)+(wallThickness/2)
    Cwe = (roomHeight/2)-(wallThickness/2)
    floorWe = -(roomHeight/2)+(wallThickness/2)
    Fwe = (roomDepth/2)-(wallThickness/2)
    Bwe = -(roomDepth/2)+(wallThickness/2)

    #Ball 1
    Xrme = xPos+ballRadius
    Xlme = xPos-ballRadius

    Yume = yPos+ballRadius
    Ybme = yPos-ballRadius

    Zfme = zPos+ballRadius
    Zbme = zPos-ballRadius

    if Xrme>=Rwe or Xlme<=Lwe:
        deltaX*=-1
    if Yume>=Cwe or Ybme<=floorWe:
        deltaY*=-1
    if Zfme>=Fwe or Zbme<=Bwe:
        deltaZ*=-1
    
    #Ball 2

    Xrme2 = xPos2+ballRadius
    Xlme2 = xPos2-ballRadius
    Yume2 = yPos2+ballRadius
    Ybme2 = yPos2-ballRadius
    Zfme2 = zPos2+ballRadius
    Zbme2 = zPos2-ballRadius

    if Xrme2>=Rwe or Xlme2<=Lwe:
        deltaX2*=-1
    if Yume2>=Cwe or Ybme2<=floorWe:
        deltaY2*=-1
    if Zfme2>=Fwe or Zbme2<=Bwe:
        deltaZ2*=-1

    #Ball 3

    
    Xrme3 = xPos3+ballRadius
    Xlme3 = xPos3-ballRadius
    Yume3 = yPos3+ballRadius
    Ybme3 = yPos3-ballRadius
    Zfme3 = zPos3+ballRadius
    Zbme3 = zPos3-ballRadius

    
    if Xrme3>=Rwe or Xlme3<=Lwe:
        deltaX3*=-1
    if Yume3>=Cwe or Ybme3<=floorWe:
        deltaY3*=-1
    if Zfme3>=Fwe or Zbme3<=Bwe:
        deltaZ3*=-1

    #Collision

    if (((Xrme>=Xlme2) and (Xlme<=Xrme2)) and ((Ybme <= Yume2) and (Yume>=Ybme2)) and ((Zfme>=Zbme2) and (Zbme<=Zfme2))):
        deltaX*=-1
        deltaX2*=-1
        deltaY*=-1
        deltaY2*=-1
        deltaZ*=-1
        deltaZ2*=-1
    if (((Xrme2>=Xlme3) and (Xlme2<=Xrme3)) and ((Ybme2 <= Yume3) and (Yume2>=Ybme3)) and ((Zfme2>=Zbme3) and (Zbme2<=Zfme3))):
        deltaX2*=-1
        deltaX3*=-1
        deltaY2*=-1
        deltaY3*=-1
        deltaZ2*=-1
        deltaZ3*=-1
    if (((Xrme>=Xlme3) and (Xlme<=Xrme3)) and ((Ybme <= Yume3) and (Yume>=Ybme3)) and ((Zfme>=Zbme3) and (Zbme<=Zfme3))):
        deltaX*=-1
        deltaX3*=-1
        deltaY*=-1
        deltaY3*=-1
        deltaZ*=-1
        deltaZ3*=-1
    

    ball1.pos=vector(xPos,yPos,zPos)
    ball2.pos=vector(xPos2,yPos2,zPos2)
    ball3.pos=vector(xPos3,yPos3,zPos3)