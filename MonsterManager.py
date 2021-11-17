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


    def __init__(self):

        monster1_Prototype = Monster1()
        monster2_Prototype = Monster2()
        monster3_Prototype = Monster3()
        monster4_Prototype = Monster4()
        # monster5_Prototype = Monster5

        # CMonsterManager.MapData = [[0 for i in range(COLUM)] for j in range(ROW)]
        # self.mapTile_Data = [[MapTile() for i in range(COLUM)] for j in range(ROW)]

        self.MonsterData = []

        self.MapStart_x = 100
        self.MapStart_y = 25

        self.pivot_x = 0
        self.pivot_y = 125

        CMonsterManager.MapData = MapTileManager.MapData
        pass


    def create_Monster(self):
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
                        monster.setSpot(MapTileManager.mapTile_Data[i][j].x, MapTileManager.mapTile_Data[i][j].y + 10,
                                        MapTileManager.mapTile_Data[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data[i][j].Tile_Width_size // 2)
                    elif Monsterindex == 2:
                        monster = Monster2()
                        monster.setSpot(MapTileManager.mapTile_Data[i][j].x, MapTileManager.mapTile_Data[i][j].y + 40,
                                        MapTileManager.mapTile_Data[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data[i][j].Tile_Width_size // 2)
                    elif Monsterindex == 3:
                        monster = Monster3()
                        monster.setSpot(MapTileManager.mapTile_Data[i][j].x, MapTileManager.mapTile_Data[i][j].y + 20,
                                        MapTileManager.mapTile_Data[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data[i][j].Tile_Width_size // 2)

                    elif Monsterindex == 4:
                        monster = Monster4()
                        monster.setSpot(MapTileManager.mapTile_Data[i][j].x, MapTileManager.mapTile_Data[i][j].y + 20,
                                        MapTileManager.mapTile_Data[i][j].Tile_Width_size // 2,
                                        MapTileManager.mapTile_Data[i][j].Tile_Width_size // 2)
                    if Monsterindex != 5:
                        self.MonsterData.append(monster)
                        game_world.add_object(monster, 1)

                elif CMonsterManager.MapData[i][j] == 2:
                    monster = Monster6()
                    monster.setSpot(MapTileManager.mapTile_Data[i][j].x - 40, MapTileManager.mapTile_Data[i][j].y - 30,0,0)

                    self.MonsterData.append(monster)
                    game_world.add_object(monster, 1)
        pass

    def update_tileSpot(self):

        pass


    def update_tileSpot_byMarioMove(self, move_prev_dst):
        # print('update tilespot')
        # for i in range(ROW - 1):
        #     for j in range(COLUM - 1):
        #         self.mapTile_Data[i][j].update_spot_byMarioMove(accumulate_dst * 2.5)
        for i in range(len(self.MonsterData)):
                self.MonsterData[i].update_spot_byMarioMove(move_prev_dst)


        pass

    def update(self):

        pass

    def draw(self):
        # for i in range(ROW -1 ):
        #     for j in range(COLUM - 1):
        #         if MapTileManager.MapData[i][j] != 0:
        #             self.mapTile_Data[i][j].draw()
        for i in range(len(self.MonsterData)):
            self.MonsterData[i].draw()



        pass







