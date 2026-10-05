from pico2d import *

CANVAS_W, CANVAS_H = 1200, 800
SCALE = 5
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

dash = [
    (1, 251, 29, 35), (36, 251, 30, 35), (74, 251, 31, 35),
    (111, 251, 31, 36), (149, 251, 30, 35), (186, 251, 31, 36),
]

peel_out = [
    (1, 207, 29, 35), (36, 207, 30, 35), (72, 208, 39, 31),
    (123, 208, 39, 32), (172, 208, 39, 31), (218, 208, 38, 32),
]

turn = [
    (1, 154, 24, 45), (31, 154, 29, 44), (65, 154, 20, 44),
    (90, 155, 25, 43), (119, 155, 25, 43), (149, 154, 20, 44),
]

hurt = [
    (184, 156, 40, 28), (232, 157, 39, 27),
]

push = [
    (1, 108, 27, 38), (31, 110, 31, 36), (64, 110, 31, 36), (99, 110, 33, 38),
    (136, 110, 32, 36), (176, 110, 33, 36), (217, 110, 33, 36), (254, 111, 33, 36),
]

surprised = [
    (6, 56, 34, 40), (49, 56, 34, 43),
]

look_around = [
    (96, 59, 23, 39), (125, 59, 23, 39),
]

# (이름, 프레임, 이동 속도[픽셀/초]) - 속도 0은 제자리 동작
ANIMATIONS = [
    ('Idle', idle, 0),
    ('Crouch', crouch, 0),
    ('Walk', walk, 150),
    ('Run', run, 300),
    ('Sprint', sprint, 450),
    ('Roll', roll, 400),
    ('Spin Dash', spin_dash, 600),
    ('Dash', dash, 500),
    ('Peel Out', peel_out, 700),
    ('Turn', turn, 0),
    ('Hurt', hurt, 0),
    ('Push', push, 50),
    ('Surprised', surprised, 0),
    ('Look Around', look_around, 0),
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
    sheet.clip_draw(left, bottom, w, h, char_x, CANVAS_H // 2, w * SCALE, h * SCALE)
    update_canvas()


def wait(seconds):
    # 기다리는 동안에도 창이 응답하도록 잘게 나눠서 이벤트를 처리한다
    end_time = get_time() + seconds
    while running and get_time() < end_time:
        handle_events()
        delay(0.01)


def play_animation(frames):
    for frame in frames:
        if not running:
            return
        draw_frame(frame)
        wait(FRAME_TIME)


def play_action(name, frames, speed):
    print(name)
    for _ in range(REPEAT_COUNT):
        if not running:
            return
        play_animation(frames)
    wait(PAUSE_TIME)


open_canvas(CANVAS_W, CANVAS_H)

sheet = load_image('sonic-sprite.png')

char_x = CANVAS_W // 2

running = True
while running:
    for name, frames, speed in ANIMATIONS:
        if not running:
            break
        play_action(name, frames, speed)

close_canvas()
