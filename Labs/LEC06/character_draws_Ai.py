from pico2d import *
from math import *

open_canvas(800, 600)
character = load_image('character.png')


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def move_line(x1, y1, x2, y2, step=5):
    # 두 점 사이를 일정한 간격으로 이동
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    count = int(distance / step)
    for i in range(count):
        t = i / count
        draw_character(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)


def move_polygon(points):
    # 꼭짓점들을 순서대로 이동하고 마지막에 시작점으로 돌아옴
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        move_line(x1, y1, x2, y2)


def move_circle(x, y, r):
    print('circle')
    for i in range(0, 360):
        draw_character(x + r * cos(radians(i)), y + r * sin(radians(i)))


def move_rectangle():
    print('rectangle')
    move_polygon([(50, 550), (750, 550), (750, 50), (50, 50)])


def move_triangle():
    print('triangle')
    move_polygon([(100, 50), (700, 50), (400, 550)])


while True:
    move_circle(400, 300, 200)
    move_rectangle()
    move_triangle()
