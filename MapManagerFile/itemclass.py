from pico2d import *

import game_world
from myEnum import *
import random
from MapManagerFile.CoinClass import *


class ItemClass:
    itemImage = None
    def __init__(self):
        if ItemClass.itemImage == None:
            ItemClass.itemImage = load_image('mario_map_tile/item.png')

        self.myCoin = CCoinClass()
        self.font = load_font('MarioFile/ENCR10B.TTF', 16)
        self.collidenum = 10
        self.ChangeColor = 0


        self.image_WIDTH = 16
        self.image_HEIGHT = 17
        self.enable = False

        self.x, self.y = 0 , 0
        self.start_x, self.start_y = 0, 0
        self.tileLength = 0


        # Tile Size in Game World
        self.Tile_Width_size = 50
        self.Tile_Height_size = 50

    def get_bb(self):
        # fill here
        return self.x - self.Tile_Width_size // 2, self.y - self.Tile_Height_size // 2\
            , self.x + self.Tile_Width_size // 2, self.y + self.Tile_Height_size // 2


    # 맵 배열의 인덱스 값을 가지고 타일들의 위치를 지정합니다.
    def setPivot(self, _x , _y, Height_index , Width_index):
        self.x = _x + self.Tile_Width_size * Width_index
        self.y = self.Tile_Height_size * Height_index  + 25

        self.start_x, self.start_y = self.x, self.y

    def setPivot2(self, _x, _y, length):
        self.tileLength = length
        self.x = _x
        self.y = _y
        self.start_x, self.start_y = self.x, self.y

        self.myCoin.setPivot2(self.x, self.y, 1)

        pass

    def update_spot_byMarioMove(self,accumulate_dist):
        if ItemClass.itemImage == None:
            pass

        # self.x = self.start_x - accumulate_dist
        self.x -= accumulate_dist
        self.myCoin.update_spot_byMarioMove(accumulate_dist)

    def lateUpdate(self):

        pass


    def update(self):
        if self.ChangeColor >= 2:
            return

        if self.collidenum < 0:
            self.ChangeColor += 1
            self.collidenum = 3

        if self.ChangeColor >= 2:
            game_world.add_object(self.myCoin, 0)

        pass

    def draw(self):

        self.font.draw(self.x- 20, self.y + 50, 'c:%d' %self.collidenum, (255, 0, 0))
        # print(self.tileLength)
        if self.tileLength == 1:
            self.itemImage.clip_draw(self.image_WIDTH * self.ChangeColor, 128 - self.image_HEIGHT,self.image_WIDTH, self.image_HEIGHT,
                                        self.x,self.y ,self.Tile_Width_size ,self.Tile_Height_size)
        elif self.tileLength == 2:
            self.itemImage.clip_draw(15, 448 - self.image_HEIGHT,self.image_WIDTH, self.image_HEIGHT,
                                        self.x,self.y ,self.Tile_Width_size * 2,self.Tile_Height_size)



        draw_rectangle(*self.get_bb())