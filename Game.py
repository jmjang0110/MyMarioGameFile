from pico2d import *
import random
import math
from MarioClass import *





def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

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

