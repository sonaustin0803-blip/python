from calendar import c
from msilib.schema import Class
from random import random
from this import s
from turtle import update
from pycat.core import Window,Sprite, KeyCode

window = Window(background_image="Copilot_20260103_151241.png")

class eagle(Sprite):
    
    def on_create(self):
        self.image='eagle.jpg'
        self.scale=0.2
    def on_update(self, dt):
        self.move_forward(10)
        if window.is_key_down(KeyCode.UP):
            self.rotation=90
        if window.is_key_down(KeyCode.DOWN):
            self.rotation=270
        if window.is_key_down(KeyCode.RIGHT):
            self.rotation=0
        if window.is_key_down(KeyCode.LEFT):
            self.rotation=180

        if self.is_touching_any_sprite():
            print('you lose')
            window.close()
        
        
            

        if self.x > 1250:
            print('you win')
            window.close()
window.create_sprite(eagle)


class s(Sprite):
    def on_create(self):
        self.image = '38.jpg'
        self.x =600
        self.y =600
class popo(Sprite):
    def on_create(self):
        self.image = 'popo.png'
        self.x =300
        self.y =300

window.create_sprite(s)
window.create_sprite(s,x=random.randint(400,740), y= 300)
window.create_sprite(s,x=750, y= 120)
window.create_sprite(popo)
window.run()