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

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
from ggame import App, Color, LineStyle, Sprite, Frame
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
yum=0



#Wall
class block(Sprite):
    asset=RectangleAsset(50, 50, thinline, black)
    def __init__(self, position):
        super(). __init__(block.asset, position)

rectangle = RectangleAsset(50, 50, thinline, black)

rounding = lambda x: 5 * round(x/5, -1)
e = []

def w(event):
    e.append(block((rounding(mouseposition[0] - 25), rounding(mouseposition[1] - 25))))
    rectangle.y = mouseposition[1]
#    print(e)


def move(event):
    global mouseposition
#    print(event.x, event.y)
    mouseposition = (event.x, event.y)


#Spring
class blockoo(Sprite):
    asset=RectangleAsset(15,4, thinline, red)
    def __init__(self, position):
        super(). __init__(blockoo.asset, position)
        self.vx=1
        self.vy=1

def s(event):
    blockoo(((mouseposition[0]), (mouseposition[1])))
    blockoo.x = mouseposition[0]
    blockoo.y = mouseposition[1]
    print(blockoo.y)
    
blockoo.go = True

def move(event):
    global mouseposition
    mouseposition = (event.x, event.y)

#Player
class blocko(Sprite):
    asset=RectangleAsset(15,30, notthinline, purple)
    def __init__(self, position):
        super(). __init__(blocko.asset, position)
        self.vx = 1
        self.vy = 1

def p(event):
    player.x=(mouseposition[0])
    player.y=(mouseposition[1])
#    print(mouseposition[0], mouseposition[1])
    t=0
player = blocko((4000,1))
player.go = True
rectangelot = RectangleAsset(15,30, notthinline, purple)


def move(event):
    global mouseposition
#    print(event.x, event.y)
    mouseposition = (event.x, event.y)


def collidingWithSprites(blocko, block):
    if blocko is block:
        return False
    elif blocko._collisionStyle == block._collisionStyle == type(blocko)._circCollision:
        dist2 = (blocko.x - block.x)**2 + (blocko.y - block.y)**2
        return dist2 < (45)**2
    else:
        return (not (blocko.xmin > block.xmax
            or blocko.xmax < block.xmin
            or blocko.ymin > block.ymax
            or blocko.ymax < block.ymin))

myapp.run()    

#class KeyEvent(_Event):
global star, yum
star = 0
def mup(event):
    star = 2
    yum=60
def might(event):
    star = 3
def meft(event):
    star = 4

global t
t=0
def step():
    global t, yum
    yum=yum-1
    if player.go:
        cc = player.collidingWithSprites(block)
        if len(cc) > 0:
            print("pancakes")
        else:
            t=t+0.05
            player.y = player.y + 3 * t
    if star == 2:
        if yum > 0:
            print("with syrup")
            t=t+2
            player.y = player.y - 3 * t
            yum = yum - 2
#        else:
#            yum = 60

    elif star == 3:
        print("and blueberries")
        player.x = player.x + 10
        star=0
    elif star == 4:
        print("chocolate chip")
        player.x = player.x - 10
        star=0
myapp.run(step)
global e
def steep():
    global e
    if blockoo.go:
        print("mooooo")
        cc = player.collidingWithSprites(block)
        if len(cc) > 0:
            print("moo")
        else:
            print("cow")
            e=e+0.05
            blockoo.y = blockoo.y + 3 * e

        
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)

myapp.run(steep)

    
myapp.listenKeyEvent('keydown' , 'w' , w)
myapp.listenMouseEvent('mousemove', move)
myapp.listenKeyEvent('keydown' , 'p' , p)
myapp.listenKeyEvent('keydown' , 's' , s)
myapp.listenKeyEvent('keydown' , 'up arrow' , mup)
myapp.listenKeyEvent('keydown' , 'right arrow' , might)
myapp.listenKeyEvent('keydown' , 'left arrow' , meft)



"""
problems:
player jumping does not work
must stop player from sinking into the walls when falling
add gravity+spring ability to the springs
make the sides of the walls collide with the player rather than just the tops

"""



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
