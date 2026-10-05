from pico2d import *

CANVAS_W, CANVAS_H = 1200, 800

open_canvas(CANVAS_W, CANVAS_H)

sheet = load_image('sonic-sprite.png')

clear_canvas()
sheet.draw(CANVAS_W // 2, CANVAS_H // 2)
update_canvas()
delay(2)

close_canvas()
