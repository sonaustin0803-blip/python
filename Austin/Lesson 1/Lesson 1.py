from logging import getLogRecordFactory
from pycat.core import Window,Sprite

window=Window()

Team=input('what is your favorite F1 TEAM?  ')
print('your favorite ', Team , ' is good')
if Team=='ferrari':
    Ferrari=window.create_sprite()
    Ferrari.image='Ferrari.jpg'
    Ferrari.scale=0.5

    Ferrari.x=640 
    Ferrari.y=320

if Team=='red bull':
    redbull=window.create_sprite()
    redbull.image='red bull.jpg'
    redbull.scale=1
    redbull.x=640 
    redbull.y=320

window.run()