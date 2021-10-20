from pico2d import *
import random
import math
from MarioClass import *

def handle_events():
    global running
    global mario1

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            mario1.ChangeDirection(Direction.RIGHT)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            mario1.ChangeDirection(Direction.LEFT)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            mario1.isJump = True
            mario1.posY = mario1.y







open_canvas()


running = True
mario1 = Mario()

while running :

    handle_events()
    clear_canvas()

#     game Logic
    mario1.update()

#     game Rendering
    mario1.draw()

    delay(0.05)

    update_canvas()

