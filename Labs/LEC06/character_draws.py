# 실습 과제 진행
from pico2d import *
from math import *

open_canvas(800, 600)

character = load_image('character.png')


def move_circle(x, y, r):
   
    print('circle')
    #캐릭터 이미지 표시
    for i in range(0, 360):
        draw_character(x + r * cos(radians(i))
                       ,y + r * sin(radians(i)))
    update_canvas()
    pass


def draw_top(x, y, b, h):
    print('top')
    for move in range(x, x + b, 5):
        draw_character(move, y + h)
    pass

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def draw_left(x, y, b, h):
    print('left')
    for move in range(y + h, y, -5):
        draw_character(x + b, move)
    pass

def draw_bottom():
    print('bottom')
    for x in range(750, 50, -5):
        draw_character(x, 50)
    pass

def draw_right():
    print('right')
    for y in range(50, 550, 5):
        draw_character(50, y)
    pass

def move_rectangle(x, y , b, h):
    print('rectangle')
    draw_top(x, y, b, h)
    draw_left(x, y, b, h)
    draw_bottom()
    draw_right()

def draw_triangle_bottom():
    print("triangle_bottom")
    for x in range(100, 700, 5):
        draw_character(x, 50)

def draw_triangle_right_up():
    print('triangle_right_up')
    lenth = 0
    for x in range(700, 400, -5):
        lenth += 5
        draw_character(x, (50 + lenth * tan(radians(45))))


def draw_triangle_left_down():
    print('triangle_left_down')
    lenth = 300
    for x in range(400, 100, -5):
        lenth -= 5
        draw_character(x, 50 + lenth * tan(radians(45)))

def move_triangle():
    print('triangle')
    draw_triangle_bottom()
    draw_triangle_right_up()
    draw_triangle_left_down()
    pass

while True:
    move_circle(400, 300, 200)
    move_rectangle(50, 50 , 700 , 500)
    move_triangle()
    pass

close_canvas()


