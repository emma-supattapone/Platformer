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
#myapp.run()

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
mouseposition = (0, 0)


class block(Sprite):
    asset=RectangleAsset(50, 50, thinline, black)
    def __init__(self, position):
        super(). __init__(block.asset, position)

rectangle = RectangleAsset(50, 50, thinline, black)

rounding = lambda x: 5 * round(x/5, -1)

def w(event):
    block((rounding(mouseposition[0] - 25), rounding(mouseposition[1] - 25)))
    rectangle.y = mouseposition[1]
    
h = myapp.listenKeyEvent('keydown' , 'w' , w)
print(h)

def move(event):
    global mouseposition
    #print(event.x, event.y)
    mouseposition = (event.x, event.y)

myapp.listenMouseEvent('mousemove', move)





class blocko(Sprite):
    asset=RectangleAsset(15,30, notthinline, purple)
    def __init__(self, position):
        super(). __init__(blocko.asset, position)

rectangelot = RectangleAsset(15,30, notthinline, purple)

rounding = lambda x: 5 * round(x/5, -1)

def p(event):
    blocko((rounding(mouseposition[0] - 25), rounding(mouseposition[1] - 25)))
    rectangle.y = mouseposition[1]
    
ho = myapp.listenKeyEvent('keydown' , 'p' , p)
print(ho)

def move(event):
    global mouseposition
    #print(event.x, event.y)
    mouseposition = (event.x, event.y)

myapp.listenMouseEvent('mousemove', move)




class blockoo(Sprite):
    asset=RectangleAsset(15,4, thinline, red)
    def __init__(self, position):
        super(). __init__(blockoo.asset, position)

rectangeloot = RectangleAsset(15,4, thinline, red)

def s(event):
    blockoo(((mouseposition[0]), (mouseposition[1])))
    rectangle.y = mouseposition[1]
    
hoo = myapp.listenKeyEvent('keydown' , 's' , s)
print(hoo)

def move(event):
    global mouseposition
    mouseposition = (event.x, event.y)

myapp.listenMouseEvent('mousemove', move)




rectangelo = RectangleAsset(15,30, thinline, orange)
circelo = CircleAsset(10, thinline, orange)




myapp.run()

x=100
y=100
poly = PolygonAsset([(x+20, y+13) , (x+22, y+18) , (x+27, y+18) , (x+22.5, y+21.5) , (x+24.5, y+26) , (x+20, y+24) , (x+15.5, y+26) , (x+17.5, y+21.5) , (x+13, y+18) ,  (x+18, y+18) , (x+20, y+13)], thinline, blue)
Sprite(poly)
x=30
y=80
Sprite(poly)
Sprite(poly)
Sprite(poly)

"""

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
Sprite(smol, (114,104))
Sprite(smol, (110,103))
Sprite(smol, (112,103))
Sprite(smol, (114,103))
Sprite(smol, (111,102))
Sprite(smol, (113,102))
#a
Sprite(smol, (117,102))
Sprite(smol, (118,102))
Sprite(smol, (116,103))
Sprite(smol, (117,104))
Sprite(smol, (118,103))
Sprite(smol, (119,104))

"""