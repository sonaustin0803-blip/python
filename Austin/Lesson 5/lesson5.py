from email.mime import image
from tkinter import Scale
import turtle
from pycat.core import Window,Sprite, KeyCode
from pycat.extensions.turtle import Turtle

window = Window()

class MovadleTurtle(Turtle):
    def on_crreate(self):
         self.pen_up()
    
    def on_update(self,dt):
        if window.is_key_pressed(KeyCode.W):
            self.y += 10
        if window.is_key_pressed(KeyCode.A):
            self.x -= 10
        if window.is_key_pressed(KeyCode.S):
            self.y -= 10
        if window.is_key_pressed(KeyCode.D):
            self.x += 10

turtle = window.create_sprite(MovadleTurtle, image='right.png', scale=0.2)

window.run()