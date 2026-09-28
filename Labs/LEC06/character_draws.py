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

def draw_bottom(x, y, b):
    print('bottom')
    for move in range(x + b, x, -5):
        draw_character(move, y)
    pass

def draw_right(x, y, h):
    print('right')
    for move in range(y, y + h, 5):
        draw_character(x, move)
    pass

def move_rectangle(x, y , b, h):
    print('rectangle')
    draw_top(x, y, b, h)
    draw_left(x, y, b, h)
    draw_bottom(x, y, b)
    draw_right(x, y, h)

def draw_triangle_bottom(x, y, b):
    print("triangle_bottom")
    for move in range(x, x + b, 5):
        draw_character(move, y)

def draw_triangle_right_up(x, y, b ,h):
    print('triangle_right_up')
    rate = h / (b / 2)
    curr_y = y
    for x in range(700, 400, -5):
        curr_y += 5 * rate
        draw_character(x, curr_y)


def draw_triangle_left_down():
    print('triangle_left_down')
    rate = 4 / 3
    h = 400
    for x in range(400, 100, -5):
        h -= 5 * rate 
        draw_character(x, 100 + h)

def move_triangle(x, y, b, h):
    print('triangle')
    draw_triangle_bottom(x, y, b)
    draw_triangle_right_up(x , y , b, h)
    draw_triangle_left_down()
    pass

while True:
    #move_circle(400, 300, 200)
    #move_rectangle(50, 50 , 700 , 500)
    move_triangle(100, 100 , 600, 400)
    pass

close_canvas()


