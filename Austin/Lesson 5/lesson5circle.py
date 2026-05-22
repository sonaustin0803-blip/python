from email.mime import image
import turtle
from pycat.core import Window,Sprite, KeyCode
from pycat.extensions.turtle import Turtle

window = Window()

turtle=window.create_sprite(Turtle, image='right.png', scale = 0.2)

turtle.position = (200,200)

turtle.pen_color
turtle.turn_left(3.14159)
turtle.move_forward(30)

for _ in range(1000):
    turtle.pen_down()
    turtle.move_forward(10)
    turtle.turn_left(3.1415926535897932)