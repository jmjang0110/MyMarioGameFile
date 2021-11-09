import random
import json
import os

from pico2d import *

import game_framework
import title_state
from MarioClass import *
from myEnum import *
from BackGround import *


name = "MainState"

mario = None
backGround = None
font = None

def enter():
    global mario, backGround
    mario = Mario()
    backGround = CBackGround()


    pass


def exit():
    global Mario, grass
    del(Mario)
    del(grass)

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

        #     움직임
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            mario.ChangeDirection(Direction.RIGHT)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            mario.ChangeDirection(Direction.LEFT)
        #     점프
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            mario.isJump = True
            mario.posY = mario.y


        #     키를 올렸을 때
        elif event.type == SDL_KEYUP and event.key != SDLK_SPACE:
            # 마리오가 점프하기 이전 방향을 저장합니다.
            mario.Save_Before_Direction()

            if mario.isJump == False:
                mario.direction = Direction.STOP
            elif mario.isJump == True:
                mario.UpdateStop_After_Jump(True)
    pass


def update():
    mario.update()
    backGround.Update(mario.accumulate_dist)


    pass


def draw():
    clear_canvas()


    backGround.draw()
    mario.draw()


    update_canvas()

    pass





