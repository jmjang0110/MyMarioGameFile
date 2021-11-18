from pico2d import *

import state_class.main_state
from myEnum import *
import random
import game_framework
import game_world
from MarioFile.Fire import *
from state_class.main_state import *


# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3 ) # 10 pixel 30 cm
# R U N
RUN_SPEED_KMPH = 15.0 # km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0) # km -> m / second
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0) # M / second
# 픽셀 단위의 속도가 구해진다.
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER) # pixel per second

# D A S H
DASH_SPEED_KMPH = 20.0 # km / Hour
DASH_SPEED_MPM = (DASH_SPEED_KMPH * 1000.0 / 60.0) # km -> m / second
DASH_SPEED_MPS = (DASH_SPEED_MPM / 60.0) # M / second
# 픽셀 단위의 속도가 구해진다.
DASH_SPEED_PPS = (DASH_SPEED_MPS * PIXEL_PER_METER) # pixel per second

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5 # 0.5초 정도 걸릴 것이다.
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION # 초당 2번 역수이므로
FRAMES_PER_ACTION = 8 # 8장 프레임



# dictionary 를 이용한 키매핑
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, \
    DASH_TIMER, DASH_DOWN, DASH_UP, JUMP_UP, JUMP_TIMER , ATTACK= range(11)

event_name = ['RIGHT_DOWN', 'LEFT_DOWN', 'RIGHT_UP', 'LEFT_UP', 'SLEEP_TIMER', \
    'DASH_TIMER', 'DASH_DOWN', 'DASH_UP' , 'JUMP_UP', 'JUMP_TIMER','SPACE']



key_event_table = {

    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,

    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,

    (SDL_KEYDOWN,SDLK_LSHIFT):DASH_DOWN,
    (SDL_KEYUP,SDLK_LSHIFT):DASH_UP,

    (SDL_KEYDOWN,SDLK_RSHIFT):DASH_DOWN,
    (SDL_KEYUP,SDLK_RSHIFT):DASH_UP,

    (SDL_KEYDOWN, SDLK_SPACE) : JUMP_UP,
    (SDL_KEYDOWN, SDLK_a) : ATTACK
}

class IdleState:
    def enter(Mario, event):
        # Mario.Speed = 0.0
        if event == RIGHT_DOWN:
            Mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            Mario.velocity += RUN_SPEED_PPS
        Mario.timer = 1000

    def exit(Mario, event):
        # if event == ATTACK:
        #     Mario.fire()

        pass

    def do(Mario):
        # frame 업데이트
        # Mario.frame = (Mario.frame + 1) % 3
        Mario.frame = (Mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        Mario.timer -= 1
        if Mario.timer == 0:
            Mario.add_event(SLEEP_TIMER)

    def draw(Mario):
        # 마리오 멈춤 / 왼쪽
        if Mario.direction == Direction.LEFT:
            Mario.image_right.clip_composite_draw(0, 588 - Mario.image_HEIGHT, Mario.image_WIDTH, Mario.image_HEIGHT,
                                             0, 'h', Mario.x, Mario.y, 100, 98)
        # 마리오 멈춤 / 오른쪽
        elif Mario.direction == Direction.RIGHT:
             Mario.image_right.clip_draw(0, 588 - Mario.image_HEIGHT, Mario.image_WIDTH, Mario.image_HEIGHT, Mario.x, Mario.y, 100, 98)



class RunState:
    def enter(Mario, event):
        if event == RIGHT_DOWN:
            Mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            Mario.velovity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            Mario.velocity += RUN_SPEED_PPS
        Mario.dir = clamp(-1, Mario.velocity, 1)
        # Mario.dir = Mario.Speed
        if (Mario.dir > 0):
            Mario.dst = 1
        else :
            Mario.dst = -1



    def exit(Mario, event):
        # if event == ATTACK:
        #     Mario.fire()
        pass

    def do(Mario):
        # FRAMES_PER_ACTION * ACTION_PER_TIME -> 초당 몇 프레임 움직이느냐
        Mario.frame = (Mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        # clmap 는 최댓값 최소값
        Mario.x = clamp(25, Mario.x, 1600 - 25)


        # 대쉬 후에 원래 속도로 조절합니다.
        if Mario.velocity < -RUN_SPEED_PPS:
            Mario.velocity = -RUN_SPEED_PPS
        elif Mario.velocity > RUN_SPEED_PPS:
            Mario.velocity = RUN_SPEED_PPS



        # frame 업데이트
        # Mario.frame = (Mario.frame + 1) % 3
        Mario.frame_Small = (Mario.frame_Small + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        if Mario.frame_Small >= 1:
           Mario.frame_Small_use = 3
        else:
            Mario.frame_Small_use = 0


        Mario.timer -= 1
        # Mario.x += Mario.Speed

        # boy.frame = (boy.frame + 1) % 8
        Mario.x += Mario.velocity * game_framework.frame_time
        if Mario.x >= WINDOW_SIZE_WIDTH // 2:
            Mario.x -= Mario.velocity * game_framework.frame_time


        Mario.move_dist += Mario.velocity * game_framework.frame_time
        Mario.move_prev_dst = (Mario.velocity * game_framework.frame_time)

        # 누적거리를 저장합니다.
        Mario.accumulate_dist += (Mario.velocity * game_framework.frame_time * Mario.dst)
        if Mario.x <= 50:
            Mario.accumulate_dist = 0

        if Mario.accumulate_dist >= WINDOW_SIZE_WIDTH:
            Mario.accumulate_dist = 0.0

        if Mario.dst < 0:
           Mario.ChangeDirection(Direction.LEFT)
        else:
           Mario.ChangeDirection(Direction.RIGHT)

        # if Mario.x <= 0:
        #    Mario.x = 0
        #    Mario.accumulate_dist = 0
        #    Mario.move_prev_dst = 0
        #    Mario.move_dist = 0
    def draw(Mario):

        # 마리오 : 오른쪽 / 이동
        if Mario.dst > 0:
            Mario.image_right.clip_draw(int(Mario.frame_Small_use) * Mario.image_WIDTH, 588 - Mario.image_HEIGHT,
                                   Mario.image_WIDTH, Mario.image_HEIGHT, Mario.x, Mario.y, 100, 98)
        # 마리오 : 왼쪽 / 이동
        else :
            Mario.image_right.clip_composite_draw(int(Mario.frame_Small_use) * Mario.image_WIDTH, 588 - Mario.image_HEIGHT,
                                         Mario.image_WIDTH, Mario.image_HEIGHT, 0, 'h', Mario.x, Mario.y, 100, 98)


class SleepState:
    def enter(Mario, event):
        Mario.frame = 0


    def exit(Mario , event):
        pass

    def do(Mario):
        # frame 업데이트
        Mario.frame = (Mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if Mario.frame_Small == 0:
            Mario.frame_Small = 3
        elif Mario.frame_Small == 3:
            Mario.frame_Small = 0

    def draw(Mario):
        # 마리오 멈춤 / 왼쪽
        if Mario.dst > 0:
            Mario.image_right.clip_composite_draw(0, 588 - Mario.image_HEIGHT, Mario.image_WIDTH, Mario.image_HEIGHT,
                                                  0, 'h', Mario.x, Mario.y, 100, 98)
        # 마리오 멈춤 / 오른쪽
        else :
            Mario.image_right.clip_draw(0, 588 - Mario.image_HEIGHT, Mario.image_WIDTH, Mario.image_HEIGHT, Mario.x,
                                        Mario.y, 100, 98)


class DashState:
    def enter(Mario, event):

        if Mario.dst > 0:
            if event == DASH_DOWN:
                Mario.velocity += DASH_SPEED_PPS
            elif event == DASH_UP:
                Mario.velocity -= DASH_SPEED_PPS
        else:
            if event == DASH_DOWN:
                Mario.velocity -= DASH_SPEED_PPS
            elif event == DASH_UP:
                Mario.velocity += DASH_SPEED_PPS

        Mario.dir = clamp(-1, Mario.velocity, 1)
        # Mario.dir = Mario.Speed
        if (Mario.dir > 0):
            Mario.dst = 1
        else:
            Mario.dst = -1

    def exit(Mario, event):
        # if event == ATTACK:
        #     Mario.fire()

        pass

    def do(Mario):
        # FRAMES_PER_ACTION * ACTION_PER_TIME -> 초당 몇 프레임 움직이느냐
        Mario.frame = (Mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        # clmap 는 최댓값 최소값
        Mario.x = clamp(25, Mario.x, 1600 - 25)

        # 대쉬 후에 원래 속도로 조절합니다.
        # if Mario.velocity < -DASH_SPEED_PPS:
        #     Mario.velocity = -DASH_SPEED_PPS
        # elif Mario.velocity > DASH_SPEED_PPS:
        #     Mario.velocity = DASH_SPEED_PPS

        # frame 업데이트
        # Mario.frame = (Mario.frame + 1) % 3
        Mario.frame_Small = (Mario.frame_Small + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        if Mario.frame_Small >= 1:
            Mario.frame_Small_use = 3
        else:
            Mario.frame_Small_use = 0

        Mario.timer -= 1
        # Mario.x += Mario.Speed

        # boy.frame = (boy.frame + 1) % 8
        Mario.x += Mario.velocity * game_framework.frame_time
        Mario.move_dist += Mario.velocity * game_framework.frame_time
        Mario.move_prev_dst = (Mario.velocity *game_framework.frame_time)
        # 누적거리를 저장합니다.
        Mario.accumulate_dist += (Mario.velocity * game_framework.frame_time * Mario.dst)
        if Mario.x <= 50:
            Mario.accumulate_dist = 0

        if Mario.accumulate_dist >= WINDOW_SIZE_WIDTH:
            Mario.accumulate_dist = 0.0

        if Mario.dst < 0:
            Mario.ChangeDirection(Direction.LEFT)
        else :
            Mario.ChangeDirection(Direction.RIGHT)


    def draw(Mario):

        # 마리오 : 오른쪽 / 이동
        if Mario.dst > 0:
            Mario.image_right.clip_draw(int(Mario.frame_Small_use) * Mario.image_WIDTH, 588 - Mario.image_HEIGHT,
                                        Mario.image_WIDTH, Mario.image_HEIGHT, Mario.x, Mario.y, 100, 98)
        # 마리오 : 왼쪽 / 이동
        else:
            Mario.image_right.clip_composite_draw(int(Mario.frame_Small_use) * Mario.image_WIDTH,
                                                  588 - Mario.image_HEIGHT,
                                                  Mario.image_WIDTH, Mario.image_HEIGHT, 0, 'h', Mario.x, Mario.y, 100,
                                                  98)


class JumpState:
    def enter(Mario, event):
        if Mario.isJump == True:
            return

        Mario.dir = clamp(-1, Mario.velocity, 1)
        # Mario.dir = Mario.Speed
        if (Mario.dir > 0):
            Mario.dst = 1
        else:
            Mario.dst = -1

        # Mario.dir = Mario.velocity
        # if (Mario.dir > 0):
        #     Mario.dst = 1
        # else:
        #     Mario.dst = -1

        Mario.isJump = True
        Mario.posY = Mario.y
        Mario.Before_State = Mario.cur_state
        pass

    def exit(Mario, event):
        pass

    def do(Mario):

        # if Mario.isJump == False:
        #     Mario.add_event(JUMP_TIMER)
            # Mario.add_event(key_event_table[Mario.Before_Key_event.type, Mario.Before_Key_event.key])
        if Mario.isJump == True:
            Mario.Jump(game_framework.frame_time)
        # frame 업데이트
        # Mario.frame = (Mario.frame + 1) % 3
        # Mario.frame = (Mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        #
        # if Mario.frame_Small == 0:
        #     Mario.frame_Small = 3
        # elif Mario.frame_Small == 3:
        #     Mario.frame_Small = 0


        Mario.timer -= 1
        Mario.x += Mario.velocity * game_framework.frame_time
        Mario.move_dist += Mario.velocity * game_framework.frame_time

        # 누적거리를 저장합니다.
        Mario.move_prev_dst =  (Mario.velocity * game_framework.frame_time )
        Mario.accumulate_dist += (Mario.velocity * game_framework.frame_time * Mario.dst)
        if Mario.x <= 50:
            Mario.accumulate_dist = 0

        if Mario.accumulate_dist >= WINDOW_SIZE_WIDTH:
            Mario.accumulate_dist = 0.0

        if Mario.x < 0:
            Mario.x = 0

    def draw(Mario):
        # 마리오 : 왼쪽 / 점프
        if Mario.dst < 0 :
             Mario.image_right.clip_composite_draw(Mario.image_WIDTH * 0, 588 + 5 - Mario.image_HEIGHT * 2,
                                         Mario.image_WIDTH, Mario.image_HEIGHT + 5, 0, 'h', Mario.x, Mario.y, 100, 98)

        # 마리오 : 오른쪽 / 점프 / 위로
        elif Mario.dst > 0:
            Mario.image_right.clip_composite_draw(Mario.image_WIDTH * 0, 588 + 5 - Mario.image_HEIGHT * 2,
                                                 Mario.image_WIDTH, Mario.image_HEIGHT + 5, 0, 'n', Mario.x, Mario.y, 100,
                                                 98)





Before_JumpState = IdleState


next_state_table = {
# fill here
# 현재 상태 : { 이벤트 : 들어갈 상태 }

    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SLEEP_TIMER: SleepState, DASH_DOWN: IdleState,
                DASH_UP: IdleState,JUMP_UP: JumpState,
                ATTACK : IdleState},

    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
               DASH_DOWN : DashState,DASH_UP: RunState,
               JUMP_UP: JumpState,
               ATTACK : RunState},

    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
                 LEFT_UP: IdleState, RIGHT_UP: IdleState,
                 DASH_DOWN: SleepState, DASH_UP : SleepState,
                 JUMP_UP: JumpState,
                 ATTACK : IdleState},

    # cur_state : { event   : 들어갈 상태 }
    DashState: { DASH_DOWN: DashState, DASH_UP: RunState,
                 RIGHT_UP: IdleState, LEFT_UP: IdleState,
                 LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
                 DASH_TIMER: RunState,JUMP_UP: JumpState,
                 ATTACK : DashState},

    JumpState: { DASH_DOWN: JumpState, DASH_UP: JumpState,
                 RIGHT_UP: JumpState, LEFT_UP: JumpState,
                 RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState,
                 JUMP_TIMER: RunState , JUMP_UP: JumpState,
                 ATTACK : JumpState}
}

class CMario:
    fireData = None

    def __init__(self):
        CMario.fireData = []

        self.image_right = load_image('mario_mainCharacter/mario_right.png')    # 500 x 588
        self.image_left = load_image('mario_mainCharacter/mario_left.png')
        self.image_Coin = load_image('mario_map_tile/item.png')
        self.image_WIDTH = 100
        self.image_HEIGHT = 98

        self.direction = Direction.RIGHT
        self.Before_direction = Direction.RIGHT
        self.jumpdirection = Direction.UP

        self.font = load_font('ENCR10B.TTF', 18)
        self.cointPoint = 0


        #  이전 키 이벤트 테이블 저장
        self.Before_Key_event = None
        self.Before_State = IdleState


        #  마리오 관련 상태변수
        self.Start_y = 150
        self.x, self.y = 50, 150
        self.timer = 0
        self.accumulate_dist = 0.0
        # 마리오가 방금 움직인 거리
        self.move_prev_dst = 0.0
        self.move_dist = 0.0

        self.velocity = 0.0
        self.dst = 1
        self.frame, self.frame_dst = 0, 1
        self.frame_Small, self.frame_Small_dst = 0, 1
        self.frame_Small_use = 0


        # 점프를 위한 변수
        self.isJump = False
        self.Stop_After_Jump = False # true 라면 점프한 후에 멈춥니다.
        self.jumpX = 10.0
        self.jumpY = self.Start_y
        self.diameter = 10.0

        self.jumpTime = 0.0
        self.jumpHeight = 0.0
        self.jumpPower = 44.0  # 이 값을 높이면 더 높이 점프 할 수 있습니다.
        self.jumpSpeed = 100   # 이 값을 높이면 점프하는 속도가 빨라집니다..
        self.posY = 0.0        # 마리오 점프 시작 위치

        self.jumpTime_dir = 1

        # 대쉬 상태를 위한 변수
        self.dashTimer = 0

        # 이벤트에 대한 상태 저장
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        # fill here
        return self.x - 20, self.y, self.x + 20, self.y + 50


    def change_state(self, state):
        # fill here
        pass

    def add_event(self, event):
        # fill here
        self.event_que.insert(0, event)
        pass

    def update(self):
        # fill here
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

            print('state : ' + self.cur_state.__name__ + 'Event : ', event_name[event])

        pass






    def handle_event(self, event):
        # fill here
        global Before_JumpState
        if event.type == SDL_KEYDOWN and event.key == SDLK_a:
            self.fire()
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == JUMP_UP:
                Before_JumpState = self.cur_state
                print("Before : ", str(Before_JumpState))

            self.add_event(key_event)


        pass


    def draw(self):
        # fill here
        draw_rectangle(*self.get_bb())
        # 마리오를 출력
        self.cur_state.draw(self)

        # 마리오 플레이 월드 상태 출력
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        self.font.draw(100, WINDOW_SIZE_HEIGHT - 20, 'WORLD : STAGE 1', (255,255,255))
        self.font.draw(100 + 200, WINDOW_SIZE_HEIGHT - 20, 'x : %2d' % self.cointPoint, (255, 255, 255))
        self.font.draw(100 + 400, WINDOW_SIZE_HEIGHT - 20, 'TIME : %3.2f' % get_time(), (255, 255, 255))
        self.image_Coin.clip_draw(1, 96,15,16, 100 + 190, WINDOW_SIZE_HEIGHT - 20, 20,20 )

        pass

    def jumpCollide_item(self):
        # self.jumpTime =  self.jumpPower - 1
        # self.jumpSpeed = 5
        self.jumpTime_dir = -1
        pass

    def Jump(self,deltatime):
        self.jumpHeight = (self.jumpTime * self.jumpTime - self.jumpPower * self.jumpTime) / 4.0
        self.jumpTime += self.jumpSpeed * game_framework.frame_time * self.jumpTime_dir
        # 마리오 : 점프에 따른 y값 조정
        self.y = self.posY + self.jumpHeight * -1

        # print(self.jumpHeight)

        # 만약에 점프하다가 벽에 부딪 쳤다면 self.jumpTime = self.jumpPower 을 하면 내려가게 됩니다.. 근데 빠르게 내려가네..?
        # if self.y + 1 >= 200:
        #     self.jumpTime = self.jumpPower - self.jumpSpeed

        if self.jumpTime >= self.jumpPower / 5 * 4:
            self.jumpdirection = Direction.DOWN
            # print('y : ', self.y, ' jumptime : ', self.jumpTime , 'jumpPower : ',self.jumpPower)

        # print(self.jumpTime, '  ',  self.jumpPower)

        if self.y < self.Start_y:
            # self.add_event(key_event_table[self.Before_Key_event.type, self.Before_Key_event.key])
            self.add_event(JUMP_TIMER)
            self.cur_state = self.Before_State

            self.jumpSpeed = 100
            self.jumpTime = 0
            self.jumpHeight = 0.0
            self.isJump = False
            self.y = self.Start_y
            self.jumpdirection = Direction.UP
            self.jumpTime_dir = 1
            if self.Stop_After_Jump == True:
                self.direction = Direction.STOP
                self.Stop_After_Jump = False


        #   캐릭터의 방향을 바꿉니다.
    def ChangeDirection(self, NewDirection):
        self.direction = NewDirection
        self.UpdateDst()

        # 방향에 따른 좌표 이동 방향을 바꿉니다.
    def UpdateDst(self):
        if self.direction == Direction.RIGHT:
            self.dst = 1
        elif self.direction == Direction.LEFT:
            self.dst = -1

    def Save_Before_Direction(self):
        #  점프 하기 이전 방향이 오른쪽이 었는지 왼쪽이었는지 업데이트 합니다.
        self.Before_direction = self.direction

    def UpdateStop_After_Jump(self, stopORgo):
        self.Stop_After_Jump = stopORgo

    def fire(self):
        makefire = Fire(self.x, self.y, self.dst * 3)
        state_class.main_state.fire.append(makefire)
        game_world.add_object(makefire,1)



