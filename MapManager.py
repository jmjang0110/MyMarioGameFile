
from pico2d import *

import state_class.server
from myEnum import *
import random
import game_framework
import game_world
from state_class.server import *



from MapManagerFile.mapTileClass import *
from MapManagerFile.GreenSewer import *
from MapManagerFile.itemclass import *
from MapManagerFile.CastleClass import *
from MapManagerFile.mountainClass import *
from MapManagerFile.mountainClass2 import *







mapTile_Prototype = None


ROW = WINDOW_SIZE_HEIGHT // 50 # 세로
COLUM = (WINDOW_SIZE_WIDTH // 50) + 20 # 가로




class MapTileManager:
    MapData_1 = []
    MapData_2 = []
    MapData_3 = []

    mapTile_Data_1 = []
    mapTile_Data_2 = []
    mapTile_Data_3 = []

    def __init__(self):
        mapTile_Prototype = MapTile()

        MapTileManager.MapData_1 = [[0 for i in range(COLUM)] for j in range(ROW)]
        MapTileManager.MapData_2 = [[0 for i in range(COLUM)] for j in range(ROW)]
        MapTileManager.MapData_3 = [[0 for i in range(COLUM)] for j in range(ROW)]

        MapTileManager.mapTile_Data_1 = [[MapTile() for i in range(COLUM)] for j in range(ROW)]
        MapTileManager.mapTile_Data_2 = [[MapTile() for i in range(COLUM)] for j in range(ROW)]
        MapTileManager.mapTile_Data_3 = [[MapTile() for i in range(COLUM)] for j in range(ROW)]

        self.MapStart_x = 100
        self.MapStart_y = 25

        self.pivot_x = 0
        self.pivot_y = 125

        pass



    def create_TileMap_byHand(self):

        # ========================================================
        #                   S T A G E 1
        # ========================================================

        # 2 층
        MapTileManager.MapData_1[1] = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1,
                                     0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        # 중간 3 : 코인 , 2 : 초록 하수구
        MapTileManager.MapData_1[2] = [0, 0, 3, 3, 3, 0, 0, 5, 5, 0, 0, 0, 0, 2, 3, 3, 0, 2, 0, 3, 3, 3, 0, 2, 0, 0, 0, 0,
                                     0, 0, 0, 2, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # 1 층
        MapTileManager.MapData_1[0] = [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1,
                                     1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 4, 0]

        # ========================================================
        #                   S T A G E 2
        # ========================================================
        # 2 층
        MapTileManager.MapData_2[1] = [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0,
                                       1,
                                       0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        # 중간 3 : 코인 , 2 : 초록 하수구
        MapTileManager.MapData_2[2] = [0, 0, 3, 3, 3, 0, 0, 5, 5, 0, 0, 0, 0, 2, 3, 3, 0, 2, 0, 3, 3, 3, 0, 2, 0, 0, 0,
                                       0,
                                       0, 0, 0, 2, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # 1 층
        MapTileManager.MapData_2[0] = [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0,
                                       1,
                                       1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 4, 0]

        pass



    def create_tileSpot_Stage1(self):
        for i in range(ROW -1):
            self.pivot_x = 0
            for j in range(COLUM-1):
                if MapTileManager.MapData_1[i][j] == 0:
                    self.pivot_x += 25
                elif MapTileManager.MapData_1[i][j] == 1:
                    self.pivot_x += 100 * MapTileManager.MapData_1[i][j]
                elif MapTileManager.MapData_1[i][j] == 2:
                    self.pivot_x += 100
                elif MapTileManager.MapData_1[i][j] == 3:
                    self.pivot_x += 50
                elif MapTileManager.MapData_1[i][j] == 5:
                    self.pivot_x += 25

                if MapTileManager.MapData_1[i][j] == 1:
                    MapTileManager.mapTile_Data_1[i][j] = MapTile()
                    MapTileManager.mapTile_Data_1[i][j].setPivot2(self.pivot_x, self.pivot_y, 1)

                elif MapTileManager.MapData_1[i][j] == 2:
                    MapTileManager.mapTile_Data_1[i][j] = CGreenSewer()
                    MapTileManager.mapTile_Data_1[i][j].setPivot2(self.pivot_x, self.pivot_y- 330, 1)

                elif MapTileManager.MapData_1[i][j] == 3:
                    MapTileManager.mapTile_Data_1[i][j] = ItemClass()
                    MapTileManager.mapTile_Data_1[i][j].setPivot2(self.pivot_x, self.pivot_y- 150 - 50, 1)


                elif MapTileManager.MapData_1[i][j] == 4:
                    MapTileManager.mapTile_Data_1[i][j] = myCastle()
                    MapTileManager.mapTile_Data_1[i][j].setPivot2(self.pivot_x, self.pivot_y + 165, 1)

                elif MapTileManager.MapData_1[i][j] == 5:
                    MapTileManager.mapTile_Data_1[i][j] = ItemClass()
                    MapTileManager.mapTile_Data_1[i][j].setPivot2(self.pivot_x, self.pivot_y - 30, 1)

                if MapTileManager.MapData_1[i][j] == 0:
                    self.pivot_x += 25
                elif MapTileManager.MapData_1[i][j] == 1:
                    self.pivot_x += 100 * MapTileManager.MapData_1[i][j]
                elif MapTileManager.MapData_1[i][j] == 2:
                    self.pivot_x += 100
                elif MapTileManager.MapData_1[i][j] == 3:
                    self.pivot_x += 10
                elif MapTileManager.MapData_1[i][j] == 5:
                    self.pivot_x += 25
            self.pivot_y += 200

        pass

    def create_tileSpot_Stage2(self):

        for i in range(ROW -1):
            self.pivot_x = 0
            for j in range(COLUM-1):
                if MapTileManager.MapData_2[i][j] == 0:
                    self.pivot_x += 25
                elif MapTileManager.MapData_2[i][j] == 1:
                    self.pivot_x += 100 * MapTileManager.MapData_2[i][j]
                elif MapTileManager.MapData_2[i][j] == 2:
                    self.pivot_x += 100
                elif MapTileManager.MapData_2[i][j] == 3:
                    self.pivot_x += 50
                elif MapTileManager.MapData_2[i][j] == 5:
                    self.pivot_x += 25

                if MapTileManager.MapData_2[i][j] == 1:
                    MapTileManager.mapTile_Data_2[i][j] = MapTile()
                    MapTileManager.mapTile_Data_2[i][j].setPivot2(self.pivot_x, self.pivot_y, 1)

                elif MapTileManager.MapData_2[i][j] == 2:
                    MapTileManager.mapTile_Data_2[i][j] = CGreenSewer()
                    MapTileManager.mapTile_Data_2[i][j].setPivot2(self.pivot_x, self.pivot_y- 330, 1)

                elif MapTileManager.MapData_2[i][j] == 3:
                    MapTileManager.mapTile_Data_2[i][j] = ItemClass()
                    MapTileManager.mapTile_Data_2[i][j].setPivot2(self.pivot_x, self.pivot_y- 150 - 50, 1)


                elif MapTileManager.MapData_2[i][j] == 4:
                    MapTileManager.mapTile_Data_2[i][j] = myCastle()
                    MapTileManager.mapTile_Data_2[i][j].setPivot2(self.pivot_x, self.pivot_y + 165, 1)

                elif MapTileManager.MapData_2[i][j] == 5:
                    MapTileManager.mapTile_Data_2[i][j] = ItemClass()
                    MapTileManager.mapTile_Data_2[i][j].setPivot2(self.pivot_x, self.pivot_y - 30, 1)

                if MapTileManager.MapData_2[i][j] == 0:
                    self.pivot_x += 25
                elif MapTileManager.MapData_2[i][j] == 1:
                    self.pivot_x += 100 * MapTileManager.MapData_2[i][j]
                elif MapTileManager.MapData_2[i][j] == 2:
                    self.pivot_x += 100
                elif MapTileManager.MapData_2[i][j] == 3:
                    self.pivot_x += 10
                elif MapTileManager.MapData_2[i][j] == 5:
                    self.pivot_x += 25
            self.pivot_y += 200

        pass
    def update_tileSpot(self):

        pass


    # def update_tileSpot_byMarioMove(self, accumulate_dst):
    #     # print('update tilespot')
    #     for i in range(ROW - 1):
    #         for j in range(COLUM - 1):
    #             MapTileManager.mapTile_Data[i][j].update_spot_byMarioMove(accumulate_dst)

    def update_tileSpot_byMarioMove(self):
        if state_class.server.mario.Stage == 1:
            # print('update tilespot')
            for i in range(ROW - 1):
                for j in range(COLUM - 1):
                    MapTileManager.mapTile_Data_1[i][j].update_spot_byMarioMove(state_class.server.mario.move_prev_dst * 2.0)

        if state_class.server.mario.Stage == 2:
            # print('update tilespot')
            for i in range(ROW - 1):
                for j in range(COLUM - 1):
                    MapTileManager.mapTile_Data_2[i][j].update_spot_byMarioMove(
                        state_class.server.mario.move_prev_dst * 2.0)

    def lateUpdate(self):
        # 마리오 움직임에 따라 타일들을 움직입니다.
        self.update_tileSpot_byMarioMove()

        pass

    def update(self):
        if state_class.server.mario.Stage == 1:
            for j in range(COLUM - 1):
                if MapTileManager.MapData_1[2][j] == 3 or MapTileManager.MapData_1[2][j] == 5:
                   MapTileManager.mapTile_Data_1[2][j].update()
        if state_class.server.mario.Stage == 2:
            for j in range(COLUM - 1):
                if MapTileManager.MapData_2[2][j] == 3 or MapTileManager.MapData_2[2][j] == 5:
                    MapTileManager.mapTile_Data_2[2][j].update()

        pass

    def draw(self):
        if state_class.server.mario.Stage == 1:
            for i in range(ROW -1 ):
                for j in range(COLUM - 1):
                    if MapTileManager.MapData_1[i][j] != 0:
                        MapTileManager.mapTile_Data_1[i][j].draw()

        if state_class.server.mario.Stage == 2:
            for i in range(ROW - 1):
                for j in range(COLUM - 1):
                    if MapTileManager.MapData_1[i][j] != 0:
                        MapTileManager.mapTile_Data_1[i][j].draw()

        pass


