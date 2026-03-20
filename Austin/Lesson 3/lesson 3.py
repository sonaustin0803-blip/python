from tracemalloc import stop
from pycat.core import Window,Sprite, KeyCode
import random

window = Window()

class Ferrari(Sprite):

    def on_create(self):
        self.image= "img/Ferrari.jpg"
        self.x=0
        self.y=300
        self.scale=0.5

    def on_update(self, dt):
        self.x += 3
        if self.x >1000:
            print("the ferrari win")    
            window.close()


class redbull (Sprite):

    def on_create(self):
        self.image= "img/red bull.jpg"
        self.x=0
        self.y=300
        self.scale=0.2
    

    def on_update(self, dt):
        if window.is_key_down(KeyCode.D):
            self.x += random.randint(50,100)
        if self.x >1000:
            print("the redbull win")    
            window.close()

window.create_sprite(Ferrari)
window.create_sprite(redbull)

window.run()
