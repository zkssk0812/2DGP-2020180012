# 실습 과제 진행
from pico2d import *
from math import *

open_canvas(800, 600)

character = load_image('character.png')


def move_circle():
    x = 400
    y = 300
    print('circle')
    #캐릭터 이미지 표시
    for i in range(0, 360):
        clear_canvas()
        character.draw(x + 200 * cos(radians(i))
                       ,y + 200 * sin(radians(i)))
        update_canvas()
        delay(0.01)
    update_canvas()
    pass

def draw_top(x, y):
    for i in range(0, 200):
        clear_canvas()
        y += i
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    update_canvas()

def draw_left(x, y):
    for i in range(0, 200):
        clear_canvas()
        x -= i
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    update_canvas()

def draw_bottom(x, y):
    for i in range(0, 200):
        clear_canvas()
        y -= i
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    update_canvas()

def draw_right(x, y):
    for i in range(0, 200):
        clear_canvas()
        x += i
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    update_canvas()

def move_rectangle():
    print('rectangle')
    x = 400
    y = 300
    draw_top(x, y)
    draw_left(x, y)
    draw_bottom(x, y)
    draw_right(x, y)
    direction = ((0, 1), (0, -1), (-1, 0), (1, 0))

def move_triangle():
    print('triangle')
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()


