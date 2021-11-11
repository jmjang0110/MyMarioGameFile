import random
import json
import os

from pico2d import *
import game_framework
import title_state
import game_world


from myEnum import *
# from MarioClass import *
from BackGround import *
from MarioClass_Test import *


name = "MainState"

mario = None
backGround = None
font = None

def enter():
    global mario, backGround
    mario = Mario()
    backGround = CBackGround()

    game_world.add_object(backGround, 0)
    game_world.add_object(mario, 1)


    pass


def exit():
    game_world.clear()


    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            mario.handle_event(event)


    pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    backGround.Update_accumulate_Dist(mario.accumulate_dist)

    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()

    pass





