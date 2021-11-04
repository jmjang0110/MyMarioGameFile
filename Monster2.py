from pico2d import *
from myEnum import *
import random

class Monster2:
    def __init__(self):
        self.image = load_image('mario_monster_sheet.png')
        self.image_WIDTH = 40
        self.image_HEIGHT = 40

        self.x, self.y = random.randint(0,WINDOW_SIZE_WIDTH - 1), 130
        self.Monster_Size_Width = 60
        self.Monster_Size_Height = 72
        self.dst = 1
        self.Speed = 2

        self.frame = 0


    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += self.Speed * self.dst

        # 왔다 갔다 설정함
        if self.x <= 0 + self.Monster_Size_Width:
            self.x = self.Monster_Size_Width
            self.dst *= -1
        elif self.x >= WINDOW_SIZE_WIDTH - self.Monster_Size_Width:
            self.x = WINDOW_SIZE_WIDTH - self.Monster_Size_Width
            self.dst *= -1

    def draw(self):
        self.image.clip_draw(112 + self.image_WIDTH * self.frame, 2426 - 90 - self.image_HEIGHT,
                             self.image_WIDTH , self.image_HEIGHT,self.x, self.y,
                             self.Monster_Size_Width, self.Monster_Size_Height)



