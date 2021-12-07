import random
import math
import game_framework
import state_class.server
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from myEnum import *

from state_class import *
from pico2d import *
from Monster_class.MonsterFire2 import *


from state_class.server import *

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


animation_names = ['Attack', 'Dead', 'Idle', 'Walk']


class Zombie:
    images = None

    def load_images(self):

        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombiefiles/female/"+ name + " (%d)" % i + ".png") for i in range(1, 11)]


    def prepare_patrol_points(self):
        # fill here
        positions = [(0, 0),(WINDOW_SIZE_WIDTH,WINDOW_SIZE_HEIGHT),(WINDOW_SIZE_WIDTH,WINDOW_SIZE_HEIGHT),
        (WINDOW_SIZE_WIDTH,WINDOW_SIZE_HEIGHT),(WINDOW_SIZE_WIDTH,WINDOW_SIZE_HEIGHT),(WINDOW_SIZE_WIDTH,WINDOW_SIZE_HEIGHT)
        ,(WINDOW_SIZE_WIDTH,WINDOW_SIZE_HEIGHT),(WINDOW_SIZE_WIDTH,WINDOW_SIZE_HEIGHT)] # 자표 획득시 기준 위치가 왼쪽 위
        self.patrol_points = []
        for p in positions:
            self.patrol_points.append((p[0], WINDOW_SIZE_HEIGHT - p[1])) # pico 2d 상의 좌표계 를 이용하도록 변경
        pass



    def __init__(self):
        self.prepare_patrol_points()
        self.patrol_order = 1 # (8 개의 좌표 )현재 어느 점 부터 수행을 할건지 지정
        self.x, self.y = self.patrol_points[0] # ( 초기위치 )


        self.x, self.y =  WINDOW_SIZE_WIDTH / 4 * 3, WINDOW_SIZE_HEIGHT / 4 * 3
        self.load_images()
        self.dir = random.random()*2*math.pi # random moving direction
        self.speed = 0
        self.timer = 1.0 # change direction every 1 sec when wandering
        self.wait_timer = 2.0
        self.frame = 0
        self.build_behavior_tree()

        self.HP = 1000
        self.FireData = []
        self.FireCount = 0

        self.fireTimer = 0.0
        self.fireTimer_Limit = 5.0
        self.firenum = 3

    def EraseMe(self):
        if self.HP <= 0:
            game_world.remove_object(self)

        pass

    def HPDown(self, Attack):
        self.HP -= Attack


    def wander(self):
        self.speed = RUN_SPEED_PPS # 좀비의 시간당 픽셀
        self.timer -= game_framework.frame_time
        # wander End
        if self.timer <= 0:
            self.timer = 10.0
            self.dir = random.random() * 2 * math.pi # 방향을 라디안 값으로 설정 ( 0 ~ 2 * PI )
            print('wabder SUCCESS ')
            return BehaviorTree.SUCCESS
        # 이렇게 SUCCESS 해줘야지 10초 기다리는 것 상관없이 플레이어를 찾으면 Chase 가 된다.
        return BehaviorTree.SUCCESS
        # wander ing
        # else:
        #     return BehaviorTree.RUNNING

        # fill here
        pass


    def wait(self):
        # fill here
        self.speed = 0
        self.wait_timer -= game_framework.frame_time
        if self.wait_timer <= 0:
            self.wait_timer = 2.0
            print('wait Success')

            return BehaviorTree.SUCCESS
        else :
            return BehaviorTree.RUNNING

        pass



    def find_player(self):
        # fill here
        distance2 = (state_class.server.mario.x - self.x)**2 + (state_class.server.mario.y - self.y)**2
        # 좀비 입장에서 보이가 10 미터 이내에 있으면 발견한 것으로 한다.
        if distance2 <= (PIXEL_PER_METER* 20)**2:
            print('find player success')
            return BehaviorTree.SUCCESS
        else:
            #  소년이 찾아지지 않으면 좀비를 멈추게 한다.
            self.speed = 0
            return BehaviorTree.FAIL

        pass

    def move_to_player(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        self.dir = math.atan2(state_class.server.mario.y - self.y , state_class.server.mario.x - self.x)
        self.fire()

        return BehaviorTree.SUCCESS # 일단 소년 쪽으로 움직이기만 해도 SUCCESS

        pass

    def get_next_position(self):
        # fill here
        self.target_x , self.target_y  = self.patrol_points[self.patrol_order % len(self.patrol_points)]
        self.patrol_order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)

        print('next Position Found Success')

        return BehaviorTree.SUCCESS

        pass

    def move_to_target(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        #  목표 지점까지 다 왔으면 SUCCESS
        # 아니면 RUNNING 리턴
        distance2 = (self.target_x - self.x)**2 + (self.target_y - self.y)**2

        # 거리가 1 미터 이내이면
        if distance2 < PIXEL_PER_METER**2:
            print('Move to target Success')
            return BehaviorTree.SUCCESS # 목적지 까지 다 왔다
        else:
            # print('Moving to target')
            return BehaviorTree.RUNNING

        pass



    def build_behavior_tree(self):
        # fill here
        wander_node = LeafNode('Wander', self.wander)
        wait_node = LeafNode('wait', self.wait)

        wander_wait_node = SequenceNode('wanderAndWait')
        wander_wait_node.add_children(wander_node, wait_node)

        get_next_position_node = LeafNode('Get Next Position', self.get_next_position)
        move_to_target_node = LeafNode('Move to Target', self.move_to_target)
        patrol_node = SequenceNode('patrol')
        patrol_node.add_children(get_next_position_node, move_to_target_node)

        find_player_node = LeafNode('Find Player',self.find_player)
        move_to_player_node = LeafNode('Move to Player', self.move_to_player)
        chase_node = SequenceNode('chase')
        chase_node.add_children(find_player_node, move_to_player_node)

        chase_wander_node = SelectorNode('chase or wander')
        chase_wander_node.add_children(chase_node, wander_node)



        self.bt = BehaviorTree(chase_wander_node)
        pass




    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        # fill here
        self.bt.run()

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(WINDOW_SIZE_WIDTH - 200, self.x, WINDOW_SIZE_WIDTH - 50)
        self.y = clamp(250 , self.y, WINDOW_SIZE_HEIGHT  - 50)


    def draw(self):
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)

    def handle_event(self, event):
        pass

    def fire(self):
        # self.FireCount += 1 * game_framework.frame_time
        self.fireTimer += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time

        if self.fireTimer >= self.fireTimer_Limit:
            self.fireTimer_Limit = 1.0
            self.fireTimer = 0.0
            self.firenum -= 1

            if self.firenum <= -1:
                self.fireTimer_Limit = 30.0
                self.firenum = 1
                self.fireTimer = 0.0

            mFire = MonsterFireBOSS(self.x, self.y, -1 * 3)
            mFire.setDir(self.dir)
            self.FireData.append(mFire)
            game_world.add_object(mFire, 1)


        if self.FireCount >= 10:
            self.FireCount = 0

        pass



