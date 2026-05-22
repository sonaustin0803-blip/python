from cgitb import text
import time
from pycat.core import Window,Sprite, KeyCode,Scheduler,RotationMode,Player,Label
import random
click = Player('gunshot.mp3')
eat = Player('dragon gun.mp3')
die = Player('die.mp3')

window = Window(background_image='background .jpg')

score_label = window.create_label(text='vegetables on ship = 0', x = 100 , y = 600)



class pizze(Sprite):

    def on_create(self):
        self.y = 500
        self.image = 'pizze.png'
        self.scale = 0.3
        self.scale_y = 0.7
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.score = 0


    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.rotation += 180
        if  self.score== 67:
            print("you win")    
            window.close()
class vegetables(Sprite):

    def on_create(self):
        self.goto_random_position()
        self.y = 50
        self.image = 'vegetables.png'
        self.scale = 0.2
        self.has_been_clicked = False

    def on_update(self, dt):
        if self.has_been_clicked == True:
            self.y += 67
        
        if self.is_touching_sprite(space_ship):
            space_ship.score +=1
            score_label.text = 'vegetables on ship = ' + str(space_ship.score)
            click.play()
            print(space_ship.score)
            time.sleep(0.5)
            self.delete()

        if self.is_touching_window_edge():
            die.play()
            space_ship.score -=1
            score_label.text = 'vegetables on ship = ' + str(space_ship.score)
            self.delete()

    def on_left_click(self):
        self.has_been_clicked = True
        eat.play()
def make_vegetables():
    window.create_sprite(vegetables)

if score_label == 10:
        print("you win")    
        window.close()

Scheduler.update(make_vegetables, 1)

space_ship = window.create_sprite(pizze)

window.run()