from pico2d import *
from myEnum import *
import random
import game_framework
from Monster_class.MonsterFire import *

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

class Monster6:
    image = None
    FireData = []
    def __init__(self):
        if Monster6.image == None:
            Monster6.image = load_image('mario_monster/mario_monster_sheet.png')

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
        pass

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
        for i in range(len(Monster6.FireData)):
            Monster6.FireData[i].update_spot_byMarioMove(move_prev_dst)



    pass

    def update(self):
        if self.enable_Show == False:
            return

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME
                       * game_framework.frame_time) % 2

        # for i in range(len(Monster6.FireData)):
        #     if Monster6.FireData[i].check_remove() == True:
        #         Monster6.FireData.remove(Monster6.FireData[i])



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


        pass
    def draw(self):
        if self.enable_Show == False:
            return

        if self.velocity >= 1:
            self.image.clip_draw(210 + int(self.frame)  * 50, 1743, self.width ,self.height,
                    self.x, self.y, 50,60)
        else:
            self.image.clip_composite_draw(205 + int(self.frame)  * 43, 1743, self.width, self.height,\
                0 , 'h', self.x, self.y, 50,60)



    pass
    def fire(self):

        mFire = MonsterFire(self.x, self.y, -1 * 3)
        # Monster6.FireData.append(mFire)
        game_world.add_object(mFire, 1)







