from pycat.core import Window,Sprite,Scheduler,KeyCode,Color
import random
window = Window(background_image='background .jpg')

class Player(Sprite):

    def on_create(self):
        self.image="pubg.png"
        self.scale = 0.05
        self.x=640
        self.y=320
        self.speed = 10
        self.position = window.center
        self.add_tag("player")

    def on_update(self,dt):
        if window.is_key_pressed(KeyCode.W):
            self.y += 10
        if window.is_key_pressed(KeyCode.A):
            self.x -= 10
        if window.is_key_pressed(KeyCode.S):
            self.y -= 10
        if window.is_key_pressed(KeyCode.D):
            self.x += 10

    def on_left_click_anywhere(self):
        window.create_sprite(bullet)

class bullet(Sprite):
    def on_create(self):
        self.image='7785269-middle.png'
        self.position = player.position
        self.speed = 10
        self.scale = 0.06
        self.point_toward_mouse_cursor()
        self.add_tag("bullet")
    def on_update(self, dt):
        self.move_forward(45)
        if self.is_touching_window_edge():
            self.delete()

class Enemy(Sprite):            

    def on_create(self):
        self.image='images (66).jpg'
        self.scale = 0.2
        self.speed = 5
        self.goto_random_position()
        self.rotation = random.randint(0,360)
        self.time = 0
        self.bullet_time = 2

    def on_update(self, dt):
        self.move_forward(self.speed)
        self.time += dt
        if self.time > self.bullet_time:
            enemy_bullet = window.create_sprite(Enemybullet)
            enemy_bullet.position = self.position
            enemy_bullet.point_toward_sprite(player)
            self.time = 0 
        
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag("bullet"):
            self.delete()

class Enemybullet(Sprite):
    def on_create(self):
        self.image='Usdollar.jpg'
        self.speed = 10
        self.scale = 0.06
        self.add_tag("enemybullet")
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag("player"):
            self.delete()

def spawn_enemy():
    window.create_sprite(Enemy)

Scheduler.update(spawn_enemy, delay=1)
player = window.create_sprite(Player)


window.run()