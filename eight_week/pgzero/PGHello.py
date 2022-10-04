import pgzrun

# define size of windows
WIDTH = 400
HEIGHT = 300


# function for draw graphics
def draw():
    screen.fill((100, 200, 150))
    screen.draw.text('Hello World', topleft=(100, 100), fontsize=30)

pgzrun.go()
