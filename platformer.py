"""
platformer.py
Author: Emma Supattapone
Credit: Abby Feyrer
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""

from ggame import App
myapp = App()
myapp.run()

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
orange = Color(0xffa500,1.0)
purple = Color(0xa020f0,1.0)
thinline = LineStyle(1, black)
notthinline = LineStyle(3, green)


class block(Sprite):
    asset=RectangleAsset(50, 50, thinline, black)
    def __init__(self, position):
        super(). __init__(block.asset, position)

rectangle = RectangleAsset(50, 50, thinline, black)
a=100
b=150
#Sprite(rectangle, (a,90))
#Sprite(rectangle, (a+b,90))

rounding = lambda x: 5 * round(x/5, -1)

def mouseClick(event):
    block((rounding(event.x - 25), rounding(event.y - 25)))
    rectangle.y = event.y

h = myapp.listenMouseEvent('click', mouseClick)
print(h)


rectangelo = RectangleAsset(15,30, thinline, orange)
Sprite(rectangelo, (100,200))
circelo = CircleAsset(10, thinline, orange)
Sprite(circelo, (107.5, 204))

rectangelot = RectangleAsset(15,30, notthinline, purple)
Sprite(rectangelot, (200, 200))
myapp = App()
myapp.run()


smol = RectangleAsset(0.1,0.1,thinline, purple)
#E
Sprite(smol, (100,100))
Sprite(smol, (100,101))
Sprite(smol, (100,102))
Sprite(smol, (100,103))
Sprite(smol, (100,104))
Sprite(smol, (101,100))
Sprite(smol, (101,102))
Sprite(smol, (101,104))
Sprite(smol, (102,100))
Sprite(smol, (102,104))
#m1
Sprite(smol, (104,104))
Sprite(smol, (106,104))
Sprite(smol, (108,104))
Sprite(smol, (104,103))
Sprite(smol, (106,103))
Sprite(smol, (108,103))
Sprite(smol, (105,102))
Sprite(smol, (107,102))
#m2
Sprite(smol, (110,104))
Sprite(smol, (112,104))
Sprite(smol, (112,104))
Sprite(smol, (110,103))
Sprite(smol, (110,103))
Sprite(smol, (112,103))
Sprite(smol, (111,102))
Sprite(smol, (113,102))

