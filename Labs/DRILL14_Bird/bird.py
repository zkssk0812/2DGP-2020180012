import random

from pico2d import load_image, get_canvas_width

import game_framework

# ---------------------------------------------------------------------------
# 스프라이트 시트 정보 (bird_animation.png : 918 x 506, 5열 x 3행, 총 14프레임)
#   - 알파 채널을 분석한 결과 프레임 간 가로 간격은 정확히 182px
#     (각 프레임의 눈 위치가 셀 기준 x=123 으로 동일 -> 좌우 떨림 없음)
#   - 세로는 506 / 3 = 168.67px 로 정수가 아니므로,
#     각 행의 위쪽 경계를 0, 169, 337 (이미지 좌표, 위->아래)로 잡고 높이 168px 사용
#   - pico2d 의 clip_draw 는 좌하단 원점이므로 bottom = 506 - top - 168
#       0행 -> 338, 1행 -> 169, 2행 -> 1
# ---------------------------------------------------------------------------
FRAME_WIDTH = 182
FRAME_HEIGHT = 168
FRAME_COLS = 5
FRAME_COUNT = 14
ROW_BOTTOMS = (338, 169, 1)

# ---------------------------------------------------------------------------
# 물리 단위 (수업 코드와 동일하게 10 pixel = 30 cm)
# ---------------------------------------------------------------------------
PIXEL_PER_METER = (10.0 / 0.3)

# 새 크기: 날개 포함 약 1.8m 폭으로 화면에 표시 (원본 182x168 비율 유지)
BIRD_WIDTH_M = 1.8
BIRD_DRAW_W = BIRD_WIDTH_M * PIXEL_PER_METER            # 약 60 px
BIRD_DRAW_H = BIRD_DRAW_W * FRAME_HEIGHT / FRAME_WIDTH  # 약 55 px

# 비행 속도: 약 20 km/h (새마다 ±20% 랜덤)
FLY_SPEED_KMPH = 20.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)        # 약 185 px/s

# 날갯짓 속도: 14프레임 한 사이클(1회 날갯짓)에 0.5초
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = FRAME_COUNT


class Bird:
    image = None  # 10마리가 같은 이미지를 공유

    def __init__(self, x=None, y=None):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')

        half_w = BIRD_DRAW_W / 2
        self.x = x if x is not None else random.uniform(half_w, get_canvas_width() - half_w)
        self.y = y if y is not None else random.uniform(250, 550)
        self.dir = random.choice((-1, 1))
        self.speed = FLY_SPEED_PPS * random.uniform(0.8, 1.2)
        # 시작 프레임을 다르게 해서 10마리가 똑같이 날갯짓하지 않도록 함
        self.frame = random.uniform(0, FRAME_COUNT)

    def update(self):
        dt = game_framework.frame_time

        # 프레임 진행: 시간 기반 (컴퓨터 속도와 무관)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * dt) % FRAME_COUNT

        # 이동 및 좌우 끝에서 방향 전환
        self.x += self.dir * self.speed * dt
        half_w = BIRD_DRAW_W / 2
        right_limit = get_canvas_width() - half_w
        if self.x > right_limit:
            self.x = right_limit
            self.dir = -1
        elif self.x < half_w:
            self.x = half_w
            self.dir = 1

    def draw(self):
        index = int(self.frame)
        col = index % FRAME_COLS
        row = index // FRAME_COLS
        left = col * FRAME_WIDTH
        bottom = ROW_BOTTOMS[row]

        if self.dir == 1:
            # 원본 이미지는 오른쪽을 보고 있음
            Bird.image.clip_draw(left, bottom, FRAME_WIDTH, FRAME_HEIGHT,
                                 self.x, self.y, BIRD_DRAW_W, BIRD_DRAW_H)
        else:
            # 왼쪽으로 날 때는 좌우 반전
            Bird.image.clip_composite_draw(left, bottom, FRAME_WIDTH, FRAME_HEIGHT,
                                           0, 'h', self.x, self.y, BIRD_DRAW_W, BIRD_DRAW_H)
