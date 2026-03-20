from multiprocessing.pool import IMapUnorderedIterator
from pycat.core import Window,Sprite
 
window=Window()

x_pos=input("enter Ferrari x position")
y_pos=input("enter Ferrari y position")

Ferrari=window.create_sprite()
Ferrari.image='Ferrari.jpg'
Ferrari.x=int(x_pos)
Ferrari.y=int(y_pos)

print(type(Ferrari.y))
print('The sprite is at position(', Ferrari.x ,',', Ferrari.y , ')has image' , Ferrari.image)

window.run()