from pico2d import *

CANVAS_W, CANVAS_H = 1200, 800
SCALE = 5

# 프레임 좌표: (left, bottom, w, h), 원점은 시트 왼쪽 아래
idle = [
    (1, 447, 29, 39), (31, 447, 26, 38), (58, 447, 28, 39), (86, 447, 30, 38), (118, 447, 30, 38),
    (150, 447, 30, 38), (182, 447, 29, 38), (211, 448, 29, 38), (240, 448, 29, 38),
]


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def draw_frame(frame):
    left, bottom, w, h = frame
    clear_canvas()
    sheet.clip_draw(left, bottom, w, h, CANVAS_W // 2, CANVAS_H // 2, w * SCALE, h * SCALE)
    update_canvas()


open_canvas(CANVAS_W, CANVAS_H)

sheet = load_image('sonic-sprite.png')

running = True
while running:
    for frame in idle:
        handle_events()
        draw_frame(frame)
        delay(0.1)

close_canvas()
