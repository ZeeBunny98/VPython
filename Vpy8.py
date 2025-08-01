from vpython import *
import numpy as np

myCylOrange = cylinder(color=color.orange, radius=1, length=6)
myCylCyan = cylinder(color = color.cyan, radius =1 , length = 6, pos=vector(0,3,0))

myCylOrangeLength = 1
myCylCyanLength = 1

myCylOrangeDelta = 0.01
myCylCyanDelta = 0.02

while True:
    rate(30)
    myCylOrangeLength = myCylOrangeLength + myCylOrangeDelta
    myCylCyanLength = myCylCyanLength + myCylCyanDelta
    myCylOrange.length = myCylOrangeLength
    myCylCyan.length = myCylCyanLength

    if (myCylOrangeLength >= 6 or myCylOrangeLength <= 0.1):
        myCylOrangeDelta *= -1
    
    if (myCylCyanLength >= 6 or myCylCyanLength <= 0.1):
        myCylCyanDelta *= -1