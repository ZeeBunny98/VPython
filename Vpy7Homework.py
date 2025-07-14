from vpython import *
import numpy as np

thermometer = box(color = color.white, size=vector(8,20,6), opacity = 0.25)
mercury = cylinder(color = color.red, radius=1, pos=vector(0,-7,0),axis=vector(0,2,0))
mercuryBall = sphere(radius=2, color=color.red, pos=vector(0,-7.5,0))
mercuryTop = sphere(color=color.red, radius=1, pos=vector(0,-4.5,0))
temperature0 = text(text="0", color = color.black, pos=vector(2,-5,3), height=1)
temperature10 = text(text="10", color = color.black, pos=vector(2,-3,3), height=1)
temperature20 = text(text="20", color = color.black, pos=vector(2,-1,3), height=1)
temperature30 = text(text="30", color = color.black, pos=vector(2,1,3), height=1)
temperature40 = text(text="40", color = color.black, pos=vector(2,3,3), height=1)
temperature50 = text(text="50", color = color.black, pos=vector(2,5,3), height=1)
temperature60 = text(text="60", color = color.black, pos=vector(2,7,3), height=1)
Celcius = text(text='°C', color=color.black, pos=vector(2.25,8.5,3), height=0.75)

thermometer2 = box(color = color.white, size=vector(8,20,6), opacity = 0.25, pos = vector(-10,0,0))
mercury2 = cylinder(color = color.red, radius=1, pos=vector(-10,-7,0),axis=vector(0,2,0))
mercuryBall2 = sphere(radius=2, color=color.red, pos=vector(-10,-7.5,0))
mercuryTop2 = sphere(color=color.red, radius=1, pos=vector(-10,-4.5,0))
temperature02 = text(text="0", color = color.black, pos=vector(-12,-5,3), height=1)
temperature102 = text(text="10", color = color.black, pos=vector(-12,-3,3), height=1)
temperature202 = text(text="20", color = color.black, pos=vector(-12,-1,3), height=1)
temperature302 = text(text="30", color = color.black, pos=vector(-12,1,3), height=1)
temperature402 = text(text="40", color = color.black, pos=vector(-12,3,3), height=1)
temperature502 = text(text="50", color = color.black, pos=vector(-12,5,3), height=1)
temperature602 = text(text="60", color = color.black, pos=vector(-12,7,3), height=1)
Celcius2 = text(text='°C', color=color.black, pos=vector(-12.25,8.5,3), height=0.75)

deltaY1 = 0.01
deltaY2 = 0.005
originalPos1 = 2
originalPos2 = 2

goingDown1 = False
goingDown2 = False

while True:
    rate(300)
    '''
    for l in np.linspace(2,28,1000):
        rate(300)
        if (l <= 14):
            mercury.axis = vector(0,l,0)
            mercuryTop.pos = vector(0,-7+l,0)

        mercury2.axis = vector(0,l/2,0)
        mercuryTop2.pos = vector(-10,-7+(l/2),0)
    '''
    if (originalPos1 < 14 and goingDown1 == False):
        originalPos1 += deltaY1
        mercury.axis = vector(0,originalPos1,0)
        mercuryTop.pos = vector(0,-7+originalPos1,0)
    
    if (originalPos2 < 14 and goingDown2 == False):
        originalPos2 += deltaY2
        mercury2.axis = vector(0,originalPos2,0)
        mercuryTop2.pos = vector(-10,-7+originalPos2,0)

    if (originalPos1 >= 14 or goingDown1 == True):
        originalPos1 -= deltaY1
        mercury.axis = vector(0,originalPos1,0)
        mercuryTop.pos = vector(0,-7+originalPos1,0)
        goingDown1 = True
        print('Going Down')
    
    if (originalPos2 >= 14 or goingDown2 == True):
        originalPos2 -= deltaY2
        mercury2.axis = vector(0,originalPos2,0)
        mercuryTop2.pos = vector(-10,-7+originalPos2,0)
        goingDown2 = True
    
    if (originalPos1 <= 2):
        goingDown1 = False
    if (originalPos2 <= 2):
        goingDown2 = False

