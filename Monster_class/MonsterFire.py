from pico2d import *
import game_framework
import game_world


# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0 # km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0 )
RUN_SPEED_MPS = ( RUN_SPEED_MPM / 60.0 )
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 5.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 100


class MonsterFire:
    image = None

    def __init__(self, x = 400, y = 300, velocity = -1):
        if MonsterFire.image == None:
            MonsterFire.image = load_image('mario_monster/mario_monster_sheet.png')
        self.x, self.y, self.velocity = x, y, RUN_SPEED_PPS * velocity
        # 점프를 위한 변수
        self.Start_y = 150

        self.image_Width = 20
        self.image_Height = 20
        self.frame = 0

        self.isJump = False
        self.Stop_After_Jump = False  # true 라면 점프한 후에 멈춥니다.
        self.jumpX = 10.0
        self.jumpY = self.Start_y
        self.diameter = 10.0

        self.jumpTime = 0.0
        self.jumpHeight = 0.0
        self.jumpPower = 45.0  # 이 값을 높이면 더 높이 점프 할 수 있습니다.
        self.jumpSpeed = 100  # 이 값을 높이면 점프하는 속도가 빨라집니다..
        self.posY = 150.0  # 마리오 점프 시작 위치

        self.DeleteTimer = 2.0

    def get_bb(self):
        # fill here
        return self.x - self.image_Width // 2 + 2, self.y - self.image_Height // 2\
            , self.x + self.image_Width // 2 - 2, self.y + self.image_Height // 2 - 3

    def draw(self):
        angle = math.atan2(self.y , self.x)
        self.image.clip_composite_draw(105 + int(self.frame) * 21 ,1753,
                                       self.image_Width,self.image_Height,0,'none',self.x,self.y,30,30)

        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        self.DeleteTimer -= 3 * game_framework.frame_time

        if self.DeleteTimer <= 0.0:
            game_world.remove_object(self)
        # self.Jump(game_framework.frame_time)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        # print(self.frame)
        #
        # # if self.x < 25 or self.x > 1600 - 25:
        # #     game_world.remove_object(self)
        # if self.jumpPower <= 3:
        #     game_world.remove_object(self)


    def Jump(self,deltatime):
        self.jumpHeight = (self.jumpTime * self.jumpTime - self.jumpPower * self.jumpTime) / 4.0
        self.jumpTime += self.jumpSpeed * game_framework.frame_time
        # 마리오 : 점프에 따른 y값 조정
        self.y = self.posY + self.jumpHeight * -1

        # if self.jumpTime >= self.jumpPower / 5 * 4:
        #     self.jumpdirection = Direction.DOWN

        if self.y < self.Start_y:
            self.jumpPower = self.jumpPower / 1.5
            self.jumpTime = 0
            self.jumpHeight = 0.0
            self.isJump = False
            self.y = self.Start_y


