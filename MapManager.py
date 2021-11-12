
from pico2d import *
from myEnum import *
import random
import game_framework
import game_world

from mapTileClass import *
mapTile_Prototype = None


ROW = WINDOW_SIZE_HEIGHT // 50 # 세로
COLUM = WINDOW_SIZE_WIDTH // 50  # 가로

MapData =[[0 for i in range(COLUM)] for j in range(ROW)]


class MapTileManager:
    def __init__(self):
        mapTile_Prototype = MapTile()

        # MapData = [[0 for i in range(COLUM)] for j in range(ROW)]
        self.mapTile_Data = [[MapTile() for i in range(COLUM)] for j in range(ROW)]

        self.MapStart_x = 25
        self.MapStart_y = 75



        pass


    def create_TileMap_byHand(self):
        MapData[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        MapData[1] = [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        MapData[2] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        MapData[3] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        MapData[4] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        MapData[5] = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        pass

    def create_tileSpot(self):
        for i in range(ROW):
            # self.MapStart_x = 25
            for j in range(COLUM):
                self.mapTile_Data[i][j].setPivot(self.MapStart_x, self.MapStart_y, i, j)
                # self.MapStart_x += 50
            # self.MapStart_y += 50

        pass


    def update(self):

        pass

    def draw(self):
        for i in range(ROW):
            for j in range(COLUM):
                if MapData[i][j] == 1:
                    self.mapTile_Data[i][j].draw()



        pass

