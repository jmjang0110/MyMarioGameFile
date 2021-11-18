from pico2d import *
from myEnum import *
import random
import game_framework
import game_world

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
FRAMES_PER_ACTION = 6 # 8장 프레임


class CCoinClass:
    itemImage = None

    def __init__(self):
        if CCoinClass.itemImage == None:
            CCoinClass.itemImage = load_image('mario_map_tile/Coinitem.png')

        self.font = load_font('MarioFile/ENCR10B.TTF', 16)

        self.coinPoint = 10 + random.randint(1, 2) * 20
        self.image_Height_Start = 777



        self.image_WIDTH = 120
        self.image_HEIGHT = 122
        self.enable = False

        self.x, self.y = 0 , 0
        self.start_x, self.start_y = 0, 0
        self.tileLength = 0
        self.frame = 0


        # Tile Size in Game World
        self.Tile_Width_size = 50
        self.Tile_Height_size = 50

    def get_bb(self):
        # fill here
        return self.x - self.Tile_Width_size // 2, self.y \
            , self.x + self.Tile_Width_size // 2, self.y + self.Tile_Height_size


    # 맵 배열의 인덱스 값을 가지고 타일들의 위치를 지정합니다.
    def setPivot(self, _x , _y, Height_index , Width_index):
        self.x = _x + self.Tile_Width_size * Width_index
        self.y = self.Tile_Height_size * Height_index  + 25

        self.start_x, self.start_y = self.x, self.y

        self.coinPoint = 10 + random.randint(0,2) * 20

        if self.coinPoint == 10:
            self.image_Height_Start = 777

        elif self.coinPoint == 30:
            self.image_Height_Start = 395

        elif self.coinPoint == 50:
            self.image_Height_Start = 140

    def setPivot2(self, _x, _y, length):
        self.tileLength = length
        self.x = _x
        self.y = _y + 25
        self.start_x, self.start_y = self.x, self.y


        if self.coinPoint == 10:
            self.image_Height_Start = 777

        elif self.coinPoint == 30:
            self.image_Height_Start = 395

        elif self.coinPoint == 50:
            self.image_Height_Start = 0
        # print(self.tileLength)
        pass

    def update_spot_byMarioMove(self,accumulate_dist):
        if CCoinClass.itemImage == None:
            pass

        # self.x = self.start_x - accumulate_dist
        self.x -= accumulate_dist


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME
                      * game_framework.frame_time) % FRAMES_PER_ACTION

        pass

    def draw(self):

        # print(self.tileLength)
        # if self.tileLength == 1:
        #     CCoinClass.itemImage.clip_draw(1, 96, 15, 16, self.x , self.y + 25, 50, 50)
        self.font.draw(self.x - 20, self.y - 50, 'p:%d' % self.coinPoint, (255, 0, 0))
        CCoinClass.itemImage.clip_draw(self.image_WIDTH * int(self.frame),  self.image_Height_Start, self.image_WIDTH, self.image_HEIGHT, self.x, self.y + 25, 50, 50)
        draw_rectangle(*self.get_bb())