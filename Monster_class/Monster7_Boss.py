from pico2d import *
from myEnum import *
import random
import game_framework
from Monster_class.MonsterFire import *
from MonsterManager import *

import game_world



# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
# R U N
RUN_SPEED_KMPH = 13.0 # km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0) # km -> m / second
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0) # M / second
# 픽셀 단위의 속도가 구해진다.
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER) # pixel per second

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.7 # 0.5초 정도 걸릴 것이다.
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION # 초당 2번 역수이므로
FRAMES_PER_ACTION = 2 # 8장 프레임

class Boss1:
    image = None

    def __init__(self):
        if Boss1.image == None:
            Boss1.image = load_image('mario_monster/mario_monster_sheet.png')



        self.HP = 1000
        self.FireData = []
        self.FireCount = 0


        self.x = random.randint(10, 200)
        self.y = 120

        self.frame = 0
        self.dir = 0
        self.velocity = RUN_SPEED_PPS

        self.width = 23
        self.height = 33

        self.dir = clamp(-1, self.velocity, 1)

        self.left_limit = 0
        self.right_limit = 0
        self.enable_Show = True
        self.start_x = 0

        self.fireTimer = 0.0
        self.fireTimer_Limit = 5.0
        self.firenum = 3

        self.HP = 1000

        pass

    def DieCheck(self):
        pass
        if self.HP <= 0:
            return True
        else:
            return False
        pass

    def HPDown(self, Attack):
        self.HP -= Attack

        pass

    def EraseMe(self):
        if self.HP <= 0:
            self.enable_Show = False
            game_world.remove_object(self)

        return self.enable_Show
        pass
    def get_bb(self):
        # fill here
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25

    def setSpot(self, x, y, left_limit, right_limit):
        self.x = x
        self.y = y + 25
        self.start_x = x

        # if self.x >= WINDOW_SIZE_WIDTH:
        #     self.enable_Show = False


        self.left_limit = self.x - left_limit
        self.right_limit = self.x + right_limit




        pass

    def update_spot_byMarioMove(self, move_prev_dst):
        self.x -= move_prev_dst
        self.update_spot_byMarioMove_Fire(move_prev_dst)

    pass

    def update_spot_byMarioMove_Fire(self,move_prev_dst):
        # FLOWER 가 발사하는 화염의 위치도 마리오 움직임에 따라 이동
        for i in range(len(self.FireData)):
            self.FireData[i].update_spot_byMarioMove(move_prev_dst)

    def lateUpdate(self):


        pass



    def update(self):
        if self.enable_Show == False:
            return

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME
                       * game_framework.frame_time) % 2

        self.fireTimer += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        if self.fireTimer >= self.fireTimer_Limit:
            self.fireTimer_Limit = 1.0
            self.fireTimer = 0.0
            self.firenum -= 1

            if self.firenum <= -1:
                self.fireTimer_Limit = 5.0
                self.firenum = 3
                self.fireTimer = 0.0
            self.fire()

        self.lateUpdate()

        pass
    def draw(self):
        if self.enable_Show == False:
            return

        if self.velocity >= 1:
            self.image.clip_draw(210 + int(self.frame)  * 50, 1743, self.width ,self.height,
                    self.x, self.y, 50,60)
        else:
            self.image.clip_composite_draw(205 + int(self.frame)  * 43, 1743, self.width, self.height,
                0 , 'h', self.x, self.y, 50,60)

        draw_rectangle(*self.get_bb())

    pass
    def fire(self):

        mFire = MonsterFire(self.x, self.y, -1 * 3)


        if self.FireCount > 3:
            self.FireCount = 0
            self.FireData.clear()
        self.FireCount += 1

        self.FireData.append(mFire)



        game_world.add_object(mFire, 1)







