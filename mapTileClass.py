from pico2d import *
from myEnum import *
import random


class MapTile:
    mapTileImage = None

    def __init__(self):
        if MapTile.mapTileImage == None:
            MapTile.mapTileImage = load_image('m_MapTileBrown.jpg')

        self.image_WIDTH = 16
        self.image_HEIGHT = 14

        self.x, self.y = 0 , 0
        # Tile Size in Game World
        self.Tile_Width_size = 50
        self.Tile_Height_size = 50


    # 맵 배열의 인덱스 값을 가지고 타일들의 위치를 지정합니다.
    def setPivot(self, _x , _y, Height_index , Width_index):
        self.x = _x + 50 * Width_index
        self.y = self.Tile_Height_size * Height_index  + 25


    def update(self):
        pass

    def draw(self):
        self.mapTileImage.clip_draw(16, 67 - self.image_HEIGHT,self.image_WIDTH, self.image_HEIGHT,
                                    self.x,self.y ,self.Tile_Width_size,self.Tile_Height_size)
