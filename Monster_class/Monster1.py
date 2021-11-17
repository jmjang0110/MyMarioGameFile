from pico2d import *
from myEnum import *
import random
import game_framework
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
TIME_PER_ACTION = 0.5 # 0.5초 정도 걸릴 것이다.
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION # 초당 2번 역수이므로
FRAMES_PER_ACTION = 8 # 8장 프레임

class Monster1:
    image = None

    def __init__(self):
        if Monster1.image == None:
            Monster1.image = load_image('mario_monster/m_Monster1.png')

        self.x = random.randint(10, 200)
        self.y = 120

        self.frame = 0
        self.dir = 0
        if random.randint(0,2)  == 1:
            self.velocity = RUN_SPEED_PPS
        else :
            self.velocity = RUN_SPEED_PPS * -1

        self.width = 62
        self.height = 40

        self.dir = clamp(-1, self.velocity, 1)

        self.left_limit = 0
        self.right_limit = 0

        self.enable_Show = True
        self.start_x = 0
        pass

    def get_bb(self):
        # fill here
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25
    def setSpot(self, x , y, left_limit, right_limit):
        self.x = x * 10 * 0.1
        self.y = (y + 25) * 10 * 0.1
        self.start_x = x

        # if self.x >= WINDOW_SIZE_WIDTH:
        #     self.enable_Show = False


        self.left_limit = self.x - left_limit
        self.right_limit = self.x + right_limit

        pass


    def update(self):
        if self.enable_Show == False:
            return

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME
                       * game_framework.frame_time) % 4

        self.x += self.velocity * game_framework.frame_time
        # self.x = clamp(25, self.x, WINDOW_SIZE_WIDTH - 25)

        if self.x < self.left_limit + 25:
            self.velocity = RUN_SPEED_PPS * 1
        if self.x > self.right_limit - 25:
            self.velocity = RUN_SPEED_PPS * -1
        # self.dir = clamp(-1, self.velocity, 1)
        pass


    def update_spot_byMarioMove(self, move_prev_dst):
        if move_prev_dst > 0:
            a = 0

        self.x -= move_prev_dst
        self.left_limit -= move_prev_dst
        self.right_limit -= move_prev_dst

        pass


    def draw(self):
        if self.enable_Show == False:
            return
        draw_rectangle(*self.get_bb())

        if self.velocity <= -1:
            self.image.clip_draw(int(self.frame)  * 62, 0, self.width ,self.height,
                    self.x, self.y)
        else:
            self.image.clip_composite_draw(int(self.frame) * 62, 0, self.width, self.height,\
                0 , 'h', self.x, self.y, self.width, self.height)



    pass






