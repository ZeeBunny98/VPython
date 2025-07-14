from vpython import *
import numpy as np

#cylinderRadius = 1
mySphere = sphere(radius=1, color=color.red, opacity=0.5)
while True:
    #for mylen in np.linspace(1,6,1000):
     #   rate(300)
      #  myPiston.length = mylen
    #for mylen in np.linspace(6,1,1000):
     #   rate(300)
      #  myPiston.length = mylen
    #for myOpacity in np.linspace(1,0,100):
     #   rate(100)
      #  myPiston.opacity = myOpacity
    #for myOpacity in np.linspace(0,1,100):
     #   rate(100)
      #  myPiston.opacity = myOpacity
    for myRadius in np.linspace(.1,1,1000):
        rate(250)
        mySphere.radius = myRadius
    for myRadius in np.linspace(1,.1,1000):
        rate(250)
        mySphere.radius = myRadius