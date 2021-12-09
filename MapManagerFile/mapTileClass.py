from pico2d import *

import state_class.server
from myEnum import *
import random

from state_class.server import *


class MapTile:
    mapTileImage = None
    mapTileImage3 = None

    def __init__(self):
        if MapTile.mapTileImage == None:
            MapTile.mapTileImage = load_image('mario_map_tile/mapObj3.png')
            MapTile.mapTileImage3 = load_image('mario_map_tile/Snowtile.png')

        self.image_WIDTH = 33
        self.image_HEIGHT = 16
        self.enable = False

        self.x, self.y = 0 , 0
        self.start_x, self.start_y = 0, 0
        self.tileLength = 0


        # Tile Size in Game World
        self.Tile_Width_size = 200
        self.Tile_Height_size = 50


    def get_bb(self):
        # fill here
        if state_class.server.mario.Stage  == 3:
            return self.x - self.Tile_Width_size // 2, self.y - (self.Tile_Height_size + 100)// 2 \
                , self.x + self.Tile_Width_size // 2, self.y + (self.Tile_Height_size + 100) // 2
        else:
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

        if state_class.server.mario.Stage == 3:
            if self.y <= 125:
                self.y -= 50

        if self.tileLength == 2:
            a = 0
        # print(self.tileLength)
        pass

    def update_spot_byMarioMove(self,accumulate_dist):
        if MapTile.mapTileImage == None:
            pass
        # self.x = self.start_x - accumulate_dist
        self.x -= accumulate_dist

    def lateUpdate(self):

        pass


    def update(self):
        pass

    def draw(self):

        if state_class.server.mario.Stage == 1:
            # print(self.tileLength)
            if self.tileLength == 1:
                self.mapTileImage.clip_draw(15, 448 - self.image_HEIGHT, self.image_WIDTH, self.image_HEIGHT,
                                            self.x, self.y, self.Tile_Width_size, self.Tile_Height_size)
            elif self.tileLength == 2:
                self.mapTileImage.clip_draw(15, 448 - self.image_HEIGHT, self.image_WIDTH, self.image_HEIGHT,
                                            self.x, self.y, self.Tile_Width_size * 2, self.Tile_Height_size)
            #draw_rectangle(*self.get_bb())

        elif state_class.server.mario.Stage == 2:
            # print(self.tileLength)
            if self.tileLength == 1:
                self.mapTileImage.clip_draw(15, 448 - self.image_HEIGHT * 3, self.image_WIDTH, self.image_HEIGHT,
                                            self.x, self.y, self.Tile_Width_size, self.Tile_Height_size)
            elif self.tileLength == 2:
                self.mapTileImage.clip_draw(15, 448 - self.image_HEIGHT, self.image_WIDTH, self.image_HEIGHT,
                                            self.x, self.y, self.Tile_Width_size * 2, self.Tile_Height_size)
            #draw_rectangle(*self.get_bb())
        elif state_class.server.mario.Stage == 3:
            # print(self.tileLength)
            if self.tileLength == 1:
                self.mapTileImage3.clip_draw(49, 140, 200, 70,
                                            self.x, self.y, self.Tile_Width_size , self.Tile_Height_size + 100)
            elif self.tileLength == 2:
                self.mapTileImage3.clip_draw(49, 140, self.image_WIDTH, self.image_HEIGHT,
                                            self.x, self.y, self.Tile_Width_size * 2, self.Tile_Height_size)
           # draw_rectangle(*self.get_bb())
