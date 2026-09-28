# 실습 과제 진행
from pico2d import *
from math import *

open_canvas(800, 600)

character = load_image('character.png')


def move_circle():
   
    print('circle')
    #캐릭터 이미지 표시
    for i in range(0, 360):
        x = 400
        y = 300
        draw_character(x + 200 * cos(radians(i))
                       ,y + 200 * sin(radians(i)))
    update_canvas()
    pass


def draw_top():
    print('top')
    for x in range(50, 750, 5):
        draw_character(x, 550)
    pass

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def draw_left():
    print('left')
    for y in range(550, 50, -5):
        draw_character(750, y)
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

def move_rectangle():
    print('rectangle')
    draw_top()
    draw_left()
    draw_bottom()
    draw_right()

def draw_triangle_bottom():
    print("triangle_bottom")
    for x in range(100, 700, 5):
        draw_character(x, 50)

def draw_triangle_right_up():
    print('triangle_right_up')

def draw_triangle_left_down():
    print('triangle_left_down')

def move_triangle():
    print('triangle')
    draw_triangle_bottom()
    draw_triangle_right_up()
    draw_triangle_left_down()
    pass

while True:
    #move_circle()
    #move_rectangle()
    move_triangle()
    pass

close_canvas()


