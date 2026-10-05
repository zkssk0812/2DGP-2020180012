from pico2d import *

CANVAS_W, CANVAS_H = 1200, 800
SCALE = 5
GROUND_Y = 150
FRAME_TIME = 0.1
REPEAT_COUNT = 5
PAUSE_TIME = 1.0

# 프레임 좌표: (left, bottom, w, h), 원점은 시트 왼쪽 아래
idle = [
    (1, 447, 29, 39), (31, 447, 26, 38), (58, 447, 28, 39), (86, 447, 30, 38), (118, 447, 30, 38),
    (150, 447, 30, 38), (182, 447, 29, 38), (211, 448, 29, 38), (240, 448, 29, 38),
]

crouch = [
    (270, 448, 24, 32), (302, 448, 29, 26),
]

walk = [
    (8, 408, 26, 37), (37, 408, 27, 37), (65, 407, 31, 38),
    (97, 408, 37, 37), (135, 410, 32, 35), (170, 408, 32, 38),
]

run = [
    (206, 408, 26, 38), (238, 408, 24, 37), (263, 408, 30, 37),
    (295, 408, 36, 37), (334, 409, 32, 36), (370, 408, 29, 38),
]

sprint = [
    (1, 361, 33, 40), (39, 362, 35, 39), (89, 362, 35, 38),
    (130, 362, 34, 42), (181, 362, 34, 41), (228, 363, 33, 40),
]

roll = [
    (1, 326, 29, 30), (35, 327, 29, 31), (67, 327, 30, 29), (98, 327, 31, 29), (131, 327, 29, 30),
    (162, 326, 29, 31), (193, 326, 30, 29), (230, 326, 31, 29), (268, 325, 30, 30),
]

spin_dash = [
    (1, 292, 30, 27), (36, 292, 29, 27), (70, 292, 29, 27),
    (105, 292, 29, 27), (139, 292, 29, 27), (174, 292, 29, 27),
]

ANIMATIONS = [
    ('Idle', idle),
    ('Crouch', crouch),
    ('Walk', walk),
    ('Run', run),
    ('Sprint', sprint),
    ('Roll', roll),
    ('Spin Dash', spin_dash),
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
    # 프레임마다 높이가 달라도 발 위치가 같도록 아래쪽을 GROUND_Y에 맞춘다
    y = GROUND_Y + h * SCALE / 2
    sheet.clip_draw(left, bottom, w, h, CANVAS_W // 2, y, w * SCALE, h * SCALE)
    update_canvas()


def wait(seconds):
    # 기다리는 동안에도 창이 응답하도록 잘게 나눠서 이벤트를 처리한다
    step = 0.01
    elapsed = 0.0
    while running and elapsed < seconds:
        handle_events()
        delay(step)
        elapsed += step


def play_animation(frames):
    for frame in frames:
        draw_frame(frame)
        wait(FRAME_TIME)


def play_action(name, frames):
    for _ in range(REPEAT_COUNT):
        play_animation(frames)
    wait(PAUSE_TIME)


open_canvas(CANVAS_W, CANVAS_H)

sheet = load_image('sonic-sprite.png')

running = True
while running:
    for name, frames in ANIMATIONS:
        play_action(name, frames)

close_canvas()
