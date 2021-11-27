from pico2d import *
from myEnum import *
import random


class myCastle:
    itemImage = None

    def __init__(self):
        if myCastle.itemImage == None:
            myCastle.itemImage = load_image('mario_map_tile/mapObj2.png')

        self.image_WIDTH = 160
        self.image_HEIGHT = 180
        self.enable = False

        self.x, self.y = 0 , 0
        self.start_x, self.start_y = 0, 0
        self.tileLength = 0


        # Tile Size in Game World
        self.Tile_Width_size = 300
        self.Tile_Height_size = 380

    def get_bb(self):
        # fill here
        return self.x - self.Tile_Width_size // 2, self.y - self.Tile_Height_size // 2\
            , self.x + self.Tile_Width_size // 2, self.y + self.Tile_Height_size // 2


    # 맵 배열의 인덱스 값을 가지고 타일들의 위치를 지정합니다.
    def setPivot(self, _x , _y, Height_index , Width_index):
        self.x = _x + self.Tile_Width_size * Width_index
        self.y = _y

        self.start_x, self.start_y = self.x, self.y

    def setPivot2(self, _x, _y, length):
        self.tileLength = length
        self.x = _x
        self.y = _y
        self.start_x, self.start_y = self.x, self.y

        if self.tileLength == 2:
            a = 0
        # print(self.tileLength)
        pass

    def update_spot_byMarioMove(self,accumulate_dist):
        if myCastle.itemImage == None:
            pass

        # self.x = self.start_x - accumulate_dist
        self.x -= accumulate_dist

    def lateUpdate(self):

        pass



    def update(self):
        pass

    def draw(self):


        # print(self.tileLength)
        if self.tileLength == 1:
            self.itemImage.clip_draw(77, 5,self.image_WIDTH, self.image_HEIGHT,
                                        self.x,self.y ,self.Tile_Width_size ,self.Tile_Height_size)
        elif self.tileLength == 2:
            self.itemImage.clip_draw(15, 448 - self.image_HEIGHT,self.image_WIDTH, self.image_HEIGHT,
                                        self.x,self.y ,self.Tile_Width_size * 2,self.Tile_Height_size)
        draw_rectangle(*self.get_bb())