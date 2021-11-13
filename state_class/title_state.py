import game_framework
from myEnum import *
from pico2d import *
import state_class.main_state



name = "TitleState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('marioTitle.png')
    pass


def exit():
    global image
    del(image)

    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else :
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(state_class.main_state)


    pass


def draw():
    clear_canvas()
    image.draw(WINDOW_SIZE_WIDTH // 2, WINDOW_SIZE_HEIGHT // 2, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)
    update_canvas()

    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






