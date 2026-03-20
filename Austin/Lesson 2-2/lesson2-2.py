from pycat.core import Window,Sprite
import random

window=Window()

class Ferrari(Sprite):
    def on_create(self):
        self.image = 'Ferrari.jpg'
        self.goto_random_position()
        self.set_random_color()
        self.rotation = random.randint(0, 180)

for _ in range(100):
    window.create_sprite(Ferrari)

window.run()
