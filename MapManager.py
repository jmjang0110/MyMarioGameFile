
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

        self.MapStart_x = 100
        self.MapStart_y = 25

        self.pivot_x = 0
        self.pivot_y = 125

        pass


    def create_TileMap_byHand(self):
        # MapData[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # MapData[1] = [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # MapData[2] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # MapData[3] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # MapData[4] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # MapData[5] = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        MapData[1] = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
        MapData[0] = [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
        pass

    def create_tileSpot(self):
        # print('create_tileSpot')
        for i in range(ROW):
            for j in range(COLUM):
                self.mapTile_Data[i][j].setPivot(self.MapStart_x, self.MapStart_y, i, j)


        pass

    def create_tileSpot2(self):
        for i in range(ROW):
            self.pivot_x = 0
            for j in range(COLUM):

                if MapData[i][j] == 0:
                    self.pivot_x += 25
                else:
                    self.pivot_x += 100 * MapData[i][j]

                self.mapTile_Data[i][j].setPivot2(self.pivot_x , self.pivot_y, MapData[i][j])

                if MapData[i][j] == 0:
                    self.pivot_x += 25
                else:
                    self.pivot_x += 100 * MapData[i][j]

            self.pivot_y += 200





        pass

    def update_tileSpot(self):

        pass


    def update_tileSpot_byMarioMove(self, accumulate_dst):
        # print('update tilespot')
        for i in range(ROW):
            for j in range(COLUM):
                self.mapTile_Data[i][j].update_spot_byMarioMove(accumulate_dst * 1.5)


    def update(self):

        pass

    def draw(self):
        for i in range(ROW):
            for j in range(COLUM):
                if MapData[i][j] != 0:
                    self.mapTile_Data[i][j].draw()



        pass

