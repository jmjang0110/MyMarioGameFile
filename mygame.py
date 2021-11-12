import game_framework
import pico2d
import start_state
import title_state
from myEnum import *

pico2d.open_canvas(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)


# game_framework.run(start_state)
game_framework.run(title_state)

pico2d.close_canvas()

# fill here
