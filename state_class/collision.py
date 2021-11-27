
from myEnum import *


# 충돌 체크
def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False


    return True

# 충돌 체크 후 부딪힌 면을 반환
def collide_plane(a, b):

    #  a 와 b 가 부딪 쳤을 때
    #  b 기준으로 부딪친 면을 반환한다.

    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return PLANE.NONE
    if right_a < left_b: return PLANE.NONE
    if top_a < bottom_b: return PLANE.NONE
    if bottom_a > top_b: return PLANE.NONE
    # 부딪침
    if (left_a <= right_b and right_b <= right_a) or (left_a <= left_b and left_b <= right_a):
            # 1. 윗면과 부딪쳤을 때
            if top_a >= bottom_b and bottom_b >= bottom_a:
                b.y = top_a + b.halfsize
                return PLANE.UP
            # 2. 윗면과 부딪쳤을 때
            elif top_b >= bottom_a and bottom_b < bottom_a:
                b.jumpTime_dir = -1
                return PLANE.DOWN
