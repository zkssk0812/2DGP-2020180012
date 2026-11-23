from pico2d import *

import game_framework
import game_world
from bird import Bird
from grass import Grass

BIRD_COUNT = 10


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def init():
    game_world.add_object(Grass(), 0)
    game_world.add_objects([Bird() for _ in range(BIRD_COUNT)], 1)


def finish():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()
