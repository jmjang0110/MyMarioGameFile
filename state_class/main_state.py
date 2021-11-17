import random
import json
import os

from pico2d import *
import game_framework
import state_class.title_state
import game_world


from myEnum import *
# from MarioClass import *
from BackGround import *
from MarioClass import *
from Monster_class.Monster1 import *
from Monster_class.Monster2 import *
from Monster_class.Monster3 import *
from Monster_class.Monster4 import *

from MapManager import *
from mapTileClass import *
from MonsterManager import *



name = "MainState"

mario = None
backGround = None
monster1 = None
monster2 = None
monster3 = None
monster4 = None
font = None


mapManager = None
monsterManager = None

maptile1 = None

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_a : return False

    return True


def enter():
    global mario, backGround,mapManager,monsterManager

    mario = Mario()
    backGround = CBackGround()
    monster1 = Monster1()
    monster2 = Monster2()
    monster3 = Monster3()
    monster4 = Monster4()
    maptile1 = MapTile()

    mapManager = MapTileManager()
    mapManager.create_TileMap_byHand()
    mapManager.create_tileSpot2()

    monsterManager = CMonsterManager()
    monsterManager.create_Monster()



    game_world.add_object(backGround, 0)
    game_world.add_object(mapManager, 0)
    game_world.add_object(monsterManager,0)

    # game_world.add_object(monster1, 1)
    # game_world.add_object(monster2, 1)
    # game_world.add_object(monster3, 1)
    # game_world.add_object(monster4, 1)
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
            game_framework.change_state(state_class.title_state)
        else:
            mario.handle_event(event)


    pass


def update():


    for game_object in game_world.all_objects():
        game_object.update()

    backGround.Update_accumulate_Dist(mario.accumulate_dist)

    mapManager.update_tileSpot_byMarioMove(mario.move_prev_dst)
    monsterManager.update_tileSpot_byMarioMove(mario.move_prev_dst)
    mario.move_prev_dst = 0

    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()

    pass





