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
from zombie import *

import state_class.server
name = "MainState"

import bgmFile

MyStage = 1
start = 1


def MonsterData_Clear():
   CMonsterManager.MonsterData.clear()




def EraseMonster():
    for i in range(len(CMonsterManager.MonsterData)):
        if CMonsterManager.MonsterData[i].DieCheck():
            del CMonsterManager.MonsterData[i]
        break

def collideCheck_withFire():

    # print('fire Num : ' ,len(state_class.server.fire))
    for k in range(len(CMonsterManager.MonsterData)):
        for  i in range(len(state_class.server.fire)):

            if collide(state_class.server.fire[i], CMonsterManager.MonsterData[k]):
                print("COLLISION")
                if CMonsterManager.MonsterData[k].enable_Show == True:
                    state_class.server.fire[i].EraseMe()

                # 충돌 된 것이므로 HP Down
                CMonsterManager.MonsterData[k].HPDown(state_class.server.fire[i].Attack)
                # Mario Fire Delete
                del state_class.server.fire[i]

                # print('del fire Num : ', len(state_class.server.fire))
                # 게임월드 내에 몬스터 remove
                if CMonsterManager.MonsterData[k].EraseMe() == True:
                    # CMonsterMAnager.MonsterData 내에 HP <= 0 인 Monster remove
                    for m in range(len(CMonsterManager.MonsterData)):
                        if m == CMonsterManager.MonsterData[k]:
                            CMonsterManager.MonsterData.remove(m)
                            del CMonsterManager.MonsterData[k]
                            break

                break
    pass

def collideCheck():
    if state_class.server.mario.Stage == 1:
        # 아이템 박스와 충돌 체크
        idx = 0
        for num in MapManager.MapTileManager.MapData_1[2]:
            # 아이템과 충돌 체크
            if num == 3 or num == 5:
                if collide(state_class.server.mario, MapManager.MapTileManager.mapTile_Data_1[2][idx]):
                    MapManager.MapTileManager.mapTile_Data_1[2][idx].collidenum -= 1
                    state_class.server.mario.jumpCollide_item()
            idx += 1

        # 마리오의 Fire 와 몬스터와의 충돌 체크
        # 1층 에서의 충돌 체크
        collideCheck_withFire()
        EraseMonster()
    elif state_class.server.mario.Stage == 2:
        # 아이템 박스와 충돌 체크
        idx = 0
        for num in MapManager.MapTileManager.MapData_2[2]:
             # 아이템과 충돌 체크
             if num == 3 or num == 5:
                if collide(state_class.server.mario, MapManager.MapTileManager.mapTile_Data_2[2][idx]):
                    MapManager.MapTileManager.mapTile_Data_2[2][idx].collidenum -= 1
                    state_class.server.mario.jumpCollide_item()
                idx += 1

        # 마리오의 Fire 와 몬스터와의 충돌 체크
        # 1층 에서의 충돌 체크
        collideCheck_withFire()
        EraseMonster()
    elif state_class.server.mario.Stage == 3:
        # 아이템 박스와 충돌 체크
        idx = 0
        for num in MapManager.MapTileManager.MapData_3[2]:
             # 아이템과 충돌 체크
             if num == 3 or num == 5:
                if collide(state_class.server.mario, MapManager.MapTileManager.mapTile_Data_3[2][idx]):
                    MapManager.MapTileManager.mapTile_Data_3[2][idx].collidenum -= 1
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

def changeStage(stage):
    game_world.clear()





def enter():
    global Stage1_BGM
    global start , MyStage


    if start == 1:
        MyStage = 1
    elif start == 2:
        MyStage = 2
    else :
        MyStage = 3

    start += 1



    game_world.clear()
    state_class.server.mario = CMario()

    state_class.server.mario.Stage = MyStage
    state_class.server.backGround = CBackGround()
    state_class.server.backGround.ChangeStage(state_class.server.mario.Stage)

    state_class.server.monster1 = Monster1()
    state_class.server.monster2 = Monster2()
    state_class.server.monster3 = Monster3()
    state_class.server.monster4 = Monster4()
    state_class.server.maptile1 = MapTile()



    # S T A G E - M A P
    state_class.server.mapManager = MapManager.MapTileManager()
    state_class.server.mapManager.create_TileMap_byHand()

    if state_class.server.mario.Stage == 1:
        state_class.server.mapManager.create_tileSpot_Stage1()
    if state_class.server.mario.Stage == 2:
        state_class.server.mapManager.create_tileSpot_Stage2()
    if state_class.server.mario.Stage == 3:
        state_class.server.mapManager.create_tileSpot_Stage3()
    # state_class.server.mapManager.create_tileSpot_Stage3()

    # M O N S T E R
    state_class.server.monsterManager = CMonsterManager()

    if state_class.server.mario.Stage == 1:
        state_class.server.monsterManager.create_Monster_Stage1()
    if state_class.server.mario.Stage == 2:
        state_class.server.monsterManager.Change_Stage(state_class.server.mario.Stage)
    if state_class.server.mario.Stage == 3:
        state_class.server.monsterManager.Change_Stage(state_class.server.mario.Stage)
        # state_class.server.monsterManager.create_Monster_Stage2()


    # A D D _ GAME WORLD
    game_world.add_object(state_class.server.backGround, 0)
    game_world.add_object(state_class.server.mapManager, 0)
    game_world.add_object(state_class.server.monsterManager,0)

    # game_world.add_object(monster1, 1)
    # game_world.add_object(monster2, 1)
    # game_world.add_object(monster3, 1)
    # game_world.add_object(monster4, 1)
    game_world.add_object(state_class.server.mario, 1)

    state_class.server.zombie = Zombie()
    game_world.add_object(state_class.server.zombie, 1)

    # state_class.server.backGround.ChangeStage(state_class.server.mario.Stage)
    # state_class.server.monsterManager.Change_Stage(state_class.server.mario.Stage)

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





