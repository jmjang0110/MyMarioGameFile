import random
import json
import os

from pico2d import *

import MapManager
import game_framework
import state_class.title_state
import game_world
from myEnum import *

# from MarioClass import *
from MapManagerFile.BackGround import *
from MarioFile.MarioClass import *

from Monster_class.Monster1 import *
from Monster_class.Monster2 import *
from Monster_class.Monster3 import *
from Monster_class.Monster4 import *

from MapManagerFile import *
from MapManagerFile.mapTileClass import *
from MonsterManager import *

import state_class.server
name = "MainState"



def EraseMonster():
    for i in range(len(CMonsterManager.MonsterData)):
        if CMonsterManager.MonsterData[i].DieCheck():
            del CMonsterManager.MonsterData[i]
        break

def collideCheck_withFire():
    idx = 0

    # print('fire Num : ' ,len(state_class.server.fire))
    for k in range(len(CMonsterManager.MonsterData)):
        for i in range(len(state_class.server.fire)):
            if collide(state_class.server.fire[i], CMonsterManager.MonsterData[k]):
                print("COLLISION")
                state_class.server.fire[i].EraseMe()
                del state_class.server.fire[i]
                # print('del fire Num : ', len(state_class.server.fire))
                CMonsterManager.MonsterData[k].HPDown(250)
                break
    idx += 1


    pass

def collideCheck():
    # 아이템 박스와 충돌 체크
    idx = 0
    for num in MapManager.MapTileManager.MapData[2]:
        # 아이템과 충돌 체크
        if num == 3 or num == 5:
            if collide(state_class.server.mario, MapManager.MapTileManager.mapTile_Data[2][idx]):
                MapManager.MapTileManager.mapTile_Data[2][idx].collidenum -= 1
                state_class.server.mario.jumpCollide_item()

        idx += 1

    # 마리오의 Fire 와 몬스터와의 충돌 체크
    # 1층 에서의 충돌 체크
    collideCheck_withFire()
    EraseMonster()
    pass

def lateUpdate():
    # 1. move stage by mario move

    # state_class.server.backGround.Update_accumulate_Dist(state_class.server.mario.accumulate_dist)
    # state_class.server.mapManager.update_tileSpot_byMarioMove(state_class.server.mario.move_prev_dst * 2.0)
    # state_class.server.monsterManager.update_tileSpot_byMarioMove(state_class.server.mario.move_prev_dst * 2.0)


    state_class.server. mapManager.lateUpdate()
    state_class.server.monsterManager.lateUpdate()
    state_class.server.mario.move_prev_dst = 0

    pass

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True


def enter():
    state_class.server.mario = CMario()
    state_class.server.backGround = CBackGround()
    state_class.server.monster1 = Monster1()
    state_class.server.monster2 = Monster2()
    state_class.server.monster3 = Monster3()
    state_class.server.monster4 = Monster4()
    state_class.server.maptile1 = MapTile()

    state_class.server.mapManager = MapManager.MapTileManager()
    state_class.server.mapManager.create_TileMap_byHand()
    state_class.server.mapManager.create_tileSpot2()

    state_class.server.monsterManager = CMonsterManager()
    state_class.server.monsterManager.create_Monster()

    game_world.add_object(state_class.server.backGround, 0)
    game_world.add_object(state_class.server.mapManager, 0)
    game_world.add_object(state_class.server.monsterManager,0)

    # game_world.add_object(monster1, 1)
    # game_world.add_object(monster2, 1)
    # game_world.add_object(monster3, 1)
    # game_world.add_object(monster4, 1)
    game_world.add_object(state_class.server.mario, 1)


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
            state_class.server.mario.handle_event(event)


    pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    lateUpdate()
    collideCheck()

    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()

    pass





