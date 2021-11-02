from pico2d import *
from myEnum import *
import random


class MapTile:
    def __init__(self):
        self.mapTileImage = load_image('m_map_tile_grass.png')
        self.image_WIDTH = 17
        self.image_HEIGHT = 15

        self.x, self.y = 22, 70

    def SetSpot(self, _x , _y, index):
        self.x = _x + 50 * index
        self.y = _y

    def UpdateDst(self, x,y):
        self.x -= x
        self.y -= y



    def draw(self):
        self.mapTileImage.clip_draw(53, 85,self.image_WIDTH, self.image_HEIGHT,self.x,self.y ,50,50)
