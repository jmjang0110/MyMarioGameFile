
from pico2d import *
from myEnum import *
import random
import game_framework
import game_world

from MapManagerFile.mapTileClass import *
from MapManagerFile.GreenSewer import *
from MapManagerFile.itemclass import *
from MapManagerFile.CastleClass import *
from MapManagerFile.mountainClass import *






mapTile_Prototype = None


ROW = WINDOW_SIZE_HEIGHT // 50 # 세로
COLUM = (WINDOW_SIZE_WIDTH // 50) + 20 # 가로




class MapTileManager:
    MapData = []
    mapTile_Data = []

    def __init__(self):
        mapTile_Prototype = MapTile()

        MapTileManager.MapData = [[0 for i in range(COLUM)] for j in range(ROW)]
        MapTileManager.mapTile_Data = [[MapTile() for i in range(COLUM)] for j in range(ROW)]

        self.MapStart_x = 100
        self.MapStart_y = 25

        self.pivot_x = 0
        self.pivot_y = 125

        pass



    def create_TileMap_byHand(self):

        # 2 층
        MapTileManager.MapData[1] = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1,
                                     0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]

        # 중간 3 : 코인 , 2 : 초록 하수구
        MapTileManager.MapData[2] = [0, 0, 3, 3, 3, 0, 0, 5, 5, 0, 0, 2, 0, 0, 5, 5, 0, 2, 0, 3, 3, 3, 0, 2, 0, 0, 0, 0,
                                     0, 0, 2, 0, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # 1 층
        MapTileManager.MapData[0] = [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0,
                                     1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 4, 0]

        pass

    def create_tileSpot(self):
        # print('create_tileSpot')
        for i in range(ROW):
            for j in range(COLUM):
                if MapTileManager.MapData[i][j] == 1:
                    MapTileManager.mapTile_Data[i][j] = MapTile()
                elif MapTileManager.MapData[i][j] == 2:
                    MapTileManager.mapTile_Data[i][j] = CGreenSewer()

                elif MapTileManager.MapData[i][j] == 3:
                    MapTileManager.mapTile_Data[i][j] = ItemClass()
                elif MapTileManager.MapData[i][j] == 4:
                    MapTileManager.mapTile_Data[i][j] = myCastle()

                MapTileManager.mapTile_Data[i][j].setPivot(self.MapStart_x, self.MapStart_y, i, j)


        pass

    def create_tileSpot2(self):
        for i in range(ROW -1):
            self.pivot_x = 0
            for j in range(COLUM-1):
                if MapTileManager.MapData[i][j] == 0:
                    self.pivot_x += 25
                elif MapTileManager.MapData[i][j] == 1:
                    self.pivot_x += 100 * MapTileManager.MapData[i][j]
                elif MapTileManager.MapData[i][j] == 2:
                    self.pivot_x += 100
                elif MapTileManager.MapData[i][j] == 3:
                    self.pivot_x += 50
                elif MapTileManager.MapData[i][j] == 5:
                    self.pivot_x += 25

                if MapTileManager.MapData[i][j] == 1:
                    MapTileManager.mapTile_Data[i][j] = MapTile()
                    MapTileManager.mapTile_Data[i][j].setPivot2(self.pivot_x, self.pivot_y, 1)

                elif MapTileManager.MapData[i][j] == 2:
                    MapTileManager.mapTile_Data[i][j] = CGreenSewer()
                    MapTileManager.mapTile_Data[i][j].setPivot2(self.pivot_x, self.pivot_y- 330, 1)

                elif MapTileManager.MapData[i][j] == 3:
                    MapTileManager.mapTile_Data[i][j] = ItemClass()
                    MapTileManager.mapTile_Data[i][j].setPivot2(self.pivot_x, self.pivot_y- 150 - 50, 1)


                elif MapTileManager.MapData[i][j] == 4:
                    MapTileManager.mapTile_Data[i][j] = myCastle()
                    MapTileManager.mapTile_Data[i][j].setPivot2(self.pivot_x, self.pivot_y + 165, 1)

                elif MapTileManager.MapData[i][j] == 5:
                    MapTileManager.mapTile_Data[i][j] = ItemClass()
                    MapTileManager.mapTile_Data[i][j].setPivot2(self.pivot_x, self.pivot_y - 30, 1)

                if MapTileManager.MapData[i][j] == 0:
                    self.pivot_x += 25
                elif MapTileManager.MapData[i][j] == 1:
                    self.pivot_x += 100 * MapTileManager.MapData[i][j]
                elif MapTileManager.MapData[i][j] == 2:
                    self.pivot_x += 100
                elif MapTileManager.MapData[i][j] == 3:
                    self.pivot_x += 10
                elif MapTileManager.MapData[i][j] == 5:
                    self.pivot_x += 25
            self.pivot_y += 200

        pass

    def update_tileSpot(self):

        pass


    def update_tileSpot_byMarioMove(self, accumulate_dst):
        # print('update tilespot')
        for i in range(ROW - 1):
            for j in range(COLUM - 1):
                MapTileManager.mapTile_Data[i][j].update_spot_byMarioMove(accumulate_dst)


    def update(self):
        for j in range(COLUM - 1):
            if MapTileManager.MapData[2][j] == 3 or MapTileManager.MapData[2][j] == 5:
               MapTileManager.mapTile_Data[2][j].update()

        pass

    def draw(self):
        for i in range(ROW -1 ):
            for j in range(COLUM - 1):
                if MapTileManager.MapData[i][j] != 0:
                    MapTileManager.mapTile_Data[i][j].draw()



        pass


