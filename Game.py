from pico2d import *
import random
import math
from myEnum import *
from MarioClass import *
from Monster1 import *


def handle_events():
    global running
    global mario1
    global monster1

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        #     키를 누르고 있을 때
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        #     움직임
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            mario1.ChangeDirection(Direction.RIGHT)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            mario1.ChangeDirection(Direction.LEFT)
        #     점프
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            mario1.isJump = True
            mario1.posY = mario1.y


        #     키를 올렸을 때
        elif event.type == SDL_KEYUP and event.key != SDLK_SPACE:
            # 마리오가 점프하기 이전 방향을 저장합니다.
            mario1.Save_Before_Direction()

            if mario1.isJump == False:
                mario1.direction = Direction.STOP
            elif mario1.isJump == True:
                mario1.UpdateStop_After_Jump(True)

open_canvas(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)

running = True
mario1 = Mario()
monster1 = Monster1()


while running :

    clear_canvas()
    handle_events()


#     game Logic
    mario1.update()
    monster1.update()

#     game Rendering
    mario1.draw()
    monster1.draw()

    delay(0.05)

    update_canvas()

