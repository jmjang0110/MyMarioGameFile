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



name = "MainState"

mario = None
fire = []
font = None

mapManager = None
backGround = None
maptile1 = None

monsterManager = None
monster1 = None
monster2 = None
monster3 = None
monster4 = None

def EraseMonster():
    for i in range(len(CMonsterManager.MonsterData)):
        if CMonsterManager.MonsterData[i].DieCheck():
            del CMonsterManager.MonsterData[i]
        break

def collideCheck_withFire():
    idx = 0
    # for num in MapManager.MapTileManager.MapData[0]:
    #     if num == 0:
    #         continue
    #     if num == 1:

    print('fire Num : ' ,len(fire))
    for k in range(len(CMonsterManager.MonsterData)):
        for i in range(len(fire)):
            if collide(fire[i], CMonsterManager.MonsterData[k]):
                print("COLLISION")
                fire[i].EraseMe()
                del fire[i]
                print('del fire Num : ', len(fire))
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
            if collide(mario, MapManager.MapTileManager.mapTile_Data[2][idx]):
                MapManager.MapTileManager.mapTile_Data[2][idx].collidenum -= 1
                mario.jumpCollide_item()

        idx += 1

    # 마리오의 Fire 와 몬스터와의 충돌 체크
    # 1층 에서의 충돌 체크
    collideCheck_withFire()
    EraseMonster()
    pass

def moveStage():
    backGround.Update_accumulate_Dist(mario.accumulate_dist)

    mapManager.update_tileSpot_byMarioMove(mario.move_prev_dst * 1.5)
    mapManager.update()

    monsterManager.update_tileSpot_byMarioMove(mario.move_prev_dst * 1.5)
    mario.move_prev_dst = 0
    pass

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

    mario = CMario()
    backGround = CBackGround()
    monster1 = Monster1()
    monster2 = Monster2()
    monster3 = Monster3()
    monster4 = Monster4()
    maptile1 = MapTile()

    mapManager = MapManager.MapTileManager()
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

    moveStage()
    collideCheck()

    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()

    pass





