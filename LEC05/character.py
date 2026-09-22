# 여기를 채우시오.



from pico2d import *
from math import *


open_canvas(800, 600)

character = load_image('character.png')

directionR = ((1, 0), (0,1), (-1, 0), (0, -1))
directionT = ((1, 0), (0, 1), (-1, -1))

while True:
    x = 400
    y = 300
    for moveX, moveY in directionR:
        for move in range(0, 200):
            clear_canvas()
            x += moveX
            y += moveY
            character.draw(x, y)
            update_canvas()
            delay(0.01)
    x = 400
    y = 300
    for i in range(0, 360 + 1):
        clear_canvas()
        character.draw(x + 100 * cos(radians(i))
                       ,y + 100 * sin(radians(i)))
        update_canvas()
        delay(0.01)
    x = 400
    y = 300
    for moveX, moveY in directionT:
        for move in range(0, 200):
            clear_canvas()
            x += moveX
            y += moveY
            character.draw(x, y)
            update_canvas()
            delay(0.01)




delay(2)

close_canvas()

