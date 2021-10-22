from pico2d import *
from myEnum import *
import random



class Monster1:
    def __init__(self):
        self.image = load_image('m_Monster1.png')
        self.image_WIDTH = 62
        self.image_HEIGHT = 40

        self.x, self.y = random.randint(0,WINDOW_SIZE_WIDTH - 1), 110
        self.Monster_Size_Width = 60
        self.Monster_Size_Height = 72





        self.frame = 0


    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x -= 3

        if self.x <= 0 + self.Monster_Size_Width:
            self.x = self.Monster_Size_Width

    def draw(self):
        self.image.clip_draw(self.image_WIDTH * self.frame, self.image_HEIGHT * 0,
                             self.image_WIDTH , self.image_HEIGHT,self.x, self.y,
                             self.Monster_Size_Width, self.Monster_Size_Height)



