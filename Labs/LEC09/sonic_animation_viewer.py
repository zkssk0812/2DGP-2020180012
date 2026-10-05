from pico2d import *

CANVAS_W, CANVAS_H = 1200, 800


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(CANVAS_W, CANVAS_H)

sheet = load_image('sonic-sprite.png')

running = True
while running:
    handle_events()
    clear_canvas()
    sheet.draw(CANVAS_W // 2, CANVAS_H // 2)
    update_canvas()
    delay(0.01)

close_canvas()
