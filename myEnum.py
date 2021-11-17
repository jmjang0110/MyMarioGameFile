from enum import Enum


class Direction(Enum):
    STOP = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    JUMP = 5
    Circle = 6

class SIZE(Enum):
    BIG = 0
    SMALL = 1

WINDOW_SIZE_WIDTH = 1200
WINDOW_SIZE_HEIGHT = 600