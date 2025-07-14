from vpython import *
import numpy as np
import requests

url = "http://api.weatherapi.com/v1/current.json"
params = {
    "key": "9a147ab93ff241159d614735251007",
    "q": "30666"
}

returned = requests.get(url,params=params)
data = returned.json()

temp = round((data["current"]["temp_c"]), -1)

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

while True:
    """
    for l in np.linspace(2,14,1000):
        rate(300)
        mercury.axis = vector(0,l,0)
        mercuryTop.pos = vector(0,-7+l,0)
    for l in np.linspace(14,2,1000):
        rate(300)
        mercury.axis = vector(0,l,0)
        mercuryTop.pos = vector(0,-7+l,0)
    """
    if (temp <= 0):
        mercury.axis=vector(0,2,0)
        mercuryTop.pos = vector(0,-7+2,0)
    if (temp == 10):
        mercury.axis=vector(0,4,0)
        mercuryTop.pos = vector(0,-7+4,0)
    if (temp == 20):
        mercury.axis=vector(0,6,0)
        mercuryTop.pos = vector(0,-7+6,0)
    if (temp == 30):
        mercury.axis=vector(0,8,0)
        mercuryTop.pos = vector(0,-7+8,0)
    if (temp == 40):
        mercury.axis=vector(0,10,0)
        mercuryTop.pos = vector(0,-7+10,0)
    if (temp == 50):
        mercury.axis=vector(0,12,0)
        mercuryTop.pos = vector(0,-7+12,0)
    if (temp == 60):
        mercury.axis=vector(0,14,0)
        mercuryTop.pos = vector(0,-7+14,0)