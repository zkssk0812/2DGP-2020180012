## 여기를 채우시오.


# 실습 과제 진행
from pico2d import *


open_canvas(800, 600)

character = load_image('character.png')

x = 300
y = 200
square_size = 200
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

while True:
    for dx, dy in directions:
        for _ in range(square_size):
            x += dx
            y += dy
            clear_canvas()
            character.draw(x, y)
            update_canvas()
            delay(0.01)