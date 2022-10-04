from random import randint
from numpy import place
import pgzrun

WIDTH = 640
HEIGHT = 480

apple = Actor('apple')

def draw():
    screen.clear()
    apple.draw()
    
def place_apple():
    apple.x = randint(10, 600)
    apple.y = randint(10, 400)
    
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print('Good Shot!')
        place_apple()
    else:
        print('You missed!')
    
place_apple()
pgzrun.go()