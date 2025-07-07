from vpython import *
from time import *

floor1 = box(pos=vector(0,-5,0),color=color.white, length=10, width=10,height=0.1)
ceiling = box(pos=vector(0,5,0),color=color.white, length=10, width=10, height=0.1)
Rwall = box(pos=vector(5,0,0), color=color.white, length=0.1,width=10,height=10)
Lwall = box(pos=vector(-5,0,0),color=color.white, length=0.1,width=10,height=10)
Bwall = box(pos=vector(0,0,-5),color=color.white, length=10,width=0.1,height=10)
ball = sphere(color=color.red, radius=0.75)

while True:
    pass