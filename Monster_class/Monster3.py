from pico2d import *
from myEnum import *
import random
import game_framework
import game_world



# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
# R U N
RUN_SPEED_KMPH = 20.0 # km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0) # km -> m / second
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0) # M / second
# 픽셀 단위의 속도가 구해진다.
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER) # pixel per second

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5 # 0.5초 정도 걸릴 것이다.
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION # 초당 2번 역수이므로
FRAMES_PER_ACTION = 8 # 8장 프레임

class Monster3:
    image = None

    def __init__(self):
        if Monster3.image == None:
            Monster3.image = load_image('mario_monster/m_Monster3.png')

        self.x = random.randint(10, 200)
        self.y = 120

        self.frame = 0
        self.dir = 0
        self.velocity = RUN_SPEED_PPS

        self.width = 30
        self.height = 40

        self.dir = clamp(-1, self.velocity, 1)

        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME
                       * game_framework.frame_time) % 4

        self.x += self.velocity * game_framework.frame_time

        self.x = clamp(25, self.x, WINDOW_SIZE_WIDTH - 25)
        if self.x <= 25 or self.x >= 800 - 25:
            self.velocity *= -1
        self.dir = clamp(-1, self.velocity, 1)



        pass
    def draw(self):
        if self.velocity >= 1:
            self.image.clip_draw(int(self.frame)  * 30, 0, self.width ,self.height,
                    self.x, self.y, 50,60)
        else:
            self.image.clip_composite_draw(int(self.frame) * 30, 0, self.width, self.height,\
                0 , 'h', self.x, self.y, 50,60)



    pass






