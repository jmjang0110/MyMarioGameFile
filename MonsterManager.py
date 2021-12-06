import MapManager

import MapManager
from Monster_class.Monster1 import *
from Monster_class.Monster2 import *
from Monster_class.Monster3 import *
from Monster_class.Monster4 import *
from Monster_class.Monster5 import *
from Monster_class.Monster6_Flower import *

from MapManager import *


from pico2d import *
from myEnum import *
import random

monster1_Prototype = None
monster2_Prototype = None
monster3_Prototype = None
monster4_Prototype = None
monster5_Prototype = None



ROW = WINDOW_SIZE_HEIGHT // 50 # 세로
COLUM = (WINDOW_SIZE_WIDTH // 50) + 20 # 가로

class CMonsterManager():
    MapData = []
    MonsterData = []

    def __init__(self):

        monster1_Prototype = Monster1()
        monster2_Prototype = Monster2()
        monster3_Prototype = Monster3()
        monster4_Prototype = Monster4()
        # monster5_Prototype = Monster5

        # CMonsterManager.MapData = [[0 for i in range(COLUM)] for j in range(ROW)]
        # self.mapTile_Data = [[MapTile() for i in range(COLUM)] for j in range(ROW)]

        self.MapStart_x = 100
        self.MapStart_y = 25

        self.pivot_x = 0
        self.pivot_y = 125

        CMonsterManager.MapData = MapManager.MapTileManager.MapData_1

        pass

    # Stage 가 바뀌면서 몬스터 정보도 업데이트 합니다.
    def Change_Stage(self, stage):
        CMonsterManager.MapData.clear()
        CMonsterManager.MonsterData.clear()

        CMonsterManager.MapData = []
        CMonsterManager.MonsterData = []


        if stage == 1:
            CMonsterManager.MapData = MapManager.MapTileManager.MapData_1
            self.create_Monster_Stage1()
        elif stage == 2:
            CMonsterManager.MapData = MapManager.MapTileManager.MapData_2
            self.create_Monster_Stage2()
        elif stage == 3:
            CMonsterManager.MapData = MapManager.MapTileManager.MapData_3




    def create_Monster_Stage1(self):

        self.MapStart_x = 100
        self.MapStart_y = 25

        self.pivot_x = 0
        self.pivot_y = 125

        # print('create_tileSpot')
        # MapData 가 1인 위치에 몬스터를 생성
        for i in range(ROW - 1):
            for j in range(COLUM - 1):
                if i == 0 and j == 0:
                    continue
                if CMonsterManager.MapData[i][j] == 1:
                    Monsterindex = random.randint(1,5)
                    if Monsterindex == 1:
                        monster = Monster1()
                        monster.setSpot(MapTileManager.mapTile_Data_1[i][j].x, MapTileManager.mapTile_Data_1[i][j].y + 10,
                                        MapTileManager.mapTile_Data_1[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data_1[i][j].Tile_Width_size // 2)
                    elif Monsterindex == 2:
                        monster = Monster2()
                        monster.setSpot(MapTileManager.mapTile_Data_1[i][j].x, MapTileManager.mapTile_Data_1[i][j].y + 40,
                                        MapTileManager.mapTile_Data_1[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data_1[i][j].Tile_Width_size // 2)
                    elif Monsterindex == 3:
                        monster = Monster3()
                        monster.setSpot(MapTileManager.mapTile_Data_1[i][j].x, MapTileManager.mapTile_Data_1[i][j].y + 20,
                                        MapTileManager.mapTile_Data_1[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data_1[i][j].Tile_Width_size // 2)

                    elif Monsterindex == 4:
                        monster = Monster4()
                        monster.setSpot(MapTileManager.mapTile_Data_1[i][j].x, MapTileManager.mapTile_Data_1[i][j].y + 20,
                                        MapTileManager.mapTile_Data_1[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data_1[i][j].Tile_Width_size // 2)
                    if Monsterindex != 5:
                        CMonsterManager.MonsterData.append(monster)
                        game_world.add_object(monster, 1)

                elif CMonsterManager.MapData[i][j] == 2:
                    monster = Monster6()
                    monster.setSpot(MapTileManager.mapTile_Data_1[i][j].x - 40, MapTileManager.mapTile_Data_1[i][j].y - 30,0,0)
                    CMonsterManager.MonsterData.append(monster)
                    game_world.add_object(monster, 1)


        pass

    def create_Monster_Stage2(self):

        self.MapStart_x = 100
        self.MapStart_y = 25

        self.pivot_x = 0
        self.pivot_y = 125

        # print('create_tileSpot')
        # MapData 가 1인 위치에 몬스터를 생성
        for i in range(ROW - 1):
            for j in range(COLUM - 1):
                if i == 0 and j == 0:
                    continue

                if CMonsterManager.MapData[i][j] == 1:
                    Monsterindex = random.randint(1, 5)
                    if Monsterindex == 1:
                        monster = Monster1()
                        monster.setSpot(MapTileManager.mapTile_Data_2[i][j].x,
                                        MapTileManager.mapTile_Data_2[i][j].y + 10,
                                        MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2)
                    elif Monsterindex == 2:
                        monster = Monster2()
                        monster.setSpot(MapTileManager.mapTile_Data_2[i][j].x,
                                        MapTileManager.mapTile_Data_2[i][j].y + 40,
                                        MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2)
                    elif Monsterindex == 3:
                        monster = Monster3()
                        monster.setSpot(MapTileManager.mapTile_Data_2[i][j].x,
                                        MapTileManager.mapTile_Data_2[i][j].y + 20,
                                        MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2)

                    elif Monsterindex == 4:
                        monster = Monster4()
                        monster.setSpot(MapTileManager.mapTile_Data_2[i][j].x,
                                        MapTileManager.mapTile_Data_2[i][j].y + 20,
                                        MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2)
                    if Monsterindex != 5:
                        CMonsterManager.MonsterData.append(monster)
                        if monster.x == 0 :
                            print(monster.x)
                        game_world.add_object(monster, 1)

                elif CMonsterManager.MapData[i][j] == 2:
                    monster = Monster6()
                    monster.setSpot(MapTileManager.mapTile_Data_2[i][j].x - 40,
                                    MapTileManager.mapTile_Data_2[i][j].y - 30, 0, 0)
                    CMonsterManager.MonsterData.append(monster)
                    game_world.add_object(monster, 1)

        # self.MapStart_x = 100
        # self.MapStart_y = 25
        #
        # self.pivot_x = 0
        # self.pivot_y = 125
        #
        # # print('create_tileSpot')
        # # MapData 가 1인 위치에 몬스터를 생성
        # for i in range(ROW - 1):
        #     for j in range(COLUM - 1):
        #         if i == 0 and j == 0:
        #             continue
        #         if CMonsterManager.MapData[i][j] == 1:
        #             Monsterindex = random.randint(1, 5)
        #             if Monsterindex == 1:
        #                 monster = Monster1()
        #                 monster.setSpot(MapTileManager.mapTile_Data_2[i][j].x,
        #                                 MapTileManager.mapTile_Data_2[i][j].y + 10,
        #                                 MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2,
        #                                 MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2)
        #             elif Monsterindex == 2:
        #                 monster = Monster2()
        #                 monster.setSpot(MapTileManager.mapTile_Data_2[i][j].x,
        #                                 MapTileManager.mapTile_Data_2[i][j].y + 40,
        #                                 MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2,
        #                                 MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2)
        #             elif Monsterindex == 3:
        #                 monster = Monster3()
        #                 monster.setSpot(MapTileManager.mapTile_Data_2[i][j].x,
        #                                 MapTileManager.mapTile_Data_2[i][j].y + 20,
        #                                 MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2,
        #                                 MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2)
        #
        #             elif Monsterindex == 4:
        #                 monster = Monster4()
        #                 monster.setSpot(MapTileManager.mapTile_Data_2[i][j].x,
        #                                 MapTileManager.mapTile_Data_2[i][j].y + 20,
        #                                 MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2,
        #                                 MapTileManager.mapTile_Data_2[i][j].Tile_Width_size // 2)
        #             if Monsterindex != 5:
        #                 CMonsterManager.MonsterData.append(monster)
        #                 game_world.add_object(monster, 1)
        #
        #         elif CMonsterManager.MapData[i][j] == 2:
        #             monster = Monster6()
        #             monster.setSpot(MapTileManager.mapTile_Data_2[i][j].x - 40,
        #                             MapTileManager.mapTile_Data_2[i][j].y - 30, 0, 0)
        #             CMonsterManager.MonsterData.append(monster)
        #             game_world.add_object(monster, 1)

        pass

    def update_tileSpot(self):

        pass


    # def update_tileSpot_byMarioMove(self, move_prev_dst):
    #     # print('update tilespot')
    #     # for i in range(ROW - 1):
    #     #     for j in range(COLUM - 1):
    #     #         self.mapTile_Data[i][j].update_spot_byMarioMove(accumulate_dst * 2.5)
    #     for i in range(len(self.MonsterData)):
    #             CMonsterManager.MonsterData[i].update_spot_byMarioMove(move_prev_dst)
    #
    #
    #     pass

    def update_tileSpot_byMarioMove(self):
        for i in range(len(self.MonsterData)):
            CMonsterManager.MonsterData[i].update_spot_byMarioMove(state_class.server.mario.move_prev_dst * 2.0)


        pass

    def lateUpdate(self):
        self.update_tileSpot_byMarioMove()

        pass


    def update(self):


        pass

    def draw(self):
        for i in range(len(self.MonsterData)):
            CMonsterManager.MonsterData[i].draw()
        pass







