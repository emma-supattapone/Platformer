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

thinline = LineStyle(1, black)

def grid(x):
    e=x%50
    if e >= 25:
        x=x+(50-e)
    if e < 25:
        x=x-e
    

class block(Sprite):
    asset=RectangleAsset(50, 50, thinline, black)
    def __init__(self, position):
        super(). __init__(block.asset, position)

rectangle = RectangleAsset(50, 50, thinline, black)
a=100
b=150
Sprite(rectangle, (a,90))
Sprite(rectangle, (a+b,90))


def mouseClick(event):
    block((grid(event.x - 25), event.y - 25))
    rectangle.y = event.y
    
h = myapp.listenMouseEvent('click', mouseClick)

print(h)



circle = CircleAsset(20, thinline, black)
Sprite(circle, (95, 80))

rectangle2 = RectangleAsset(35, 60, thinline, red)


Sprite(rectangle2, (100, 170))





myapp = App()
myapp.run()

"""
rectangle = RectangleAsset()


rectangle3 = RectangleAsset(200, 210, thinline, blue)
rectangle4 = RectangleAsset(20, 800, thinline, red)

circle2 = CircleAsset(10, thinline, white)
polygon = PolygonAsset([(200, 130) , (220, 180) , (270, 180) , (225, 215) , (245, 260) , (200, 240) , (155, 260) , (175, 215) , (130, 180) ,  (180, 180) , (200, 130)], thinline, white)
ellipse = EllipseAsset(20, 300, thinline, black)

# Creating sprites
Sprite(rectangle, (300, 100))
Sprite(rectangle, (300, 170))
Sprite(rectangle, (300, 240))

Sprite(rectangle2, (100, 380))
Sprite(rectangle2, (100, 450))
Sprite(rectangle3,(100,100))

Sprite(circle2, (95, 80))
Sprite(polygon, (0, 0))
Sprite(ellipse, (100, 400))

# add your code here /\  /\  /\
"""
