# Game Shoot the fruit
import pgzrun
from random import randint
# define size of the windows
WIDTH = 640
HEIGHT = 480

# create object
apple = Actor('apple')


# function for display
def draw():
    screen.clear()
    apple.draw()


# function random position of apple
def place_apple():
    apple.x = randint(10, 600)
    apple.y = randint(10, 400)


# function to get mouse event
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print('Good Shot!')
        place_apple()
    else:
        print('You missed!')


place_apple()
pgzrun.go()
