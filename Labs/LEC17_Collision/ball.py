from pico2d import get_canvas_width, load_image, draw_rectangle

import game_world
import game_framework

# 단위: 픽셀, 초
LAUNCH_SPEED_X = 300.0
LAUNCH_SPEED_Y = 300.0
GRAVITY = 9.8 * (10.0 / 0.3)  # 9.8 m/s²를 픽셀/s²로 변환
GROUND_Y = 40


class Ball:
    images = {}

    def __init__(self, x, y, direction, ball_type=1):
        if ball_type not in Ball.images:
            Ball.images[ball_type] = load_image(
                'ball21x21.png' if ball_type == 1 else 'ball41x41.png')
        self.image = Ball.images[ball_type]
        self.x, self.y = x, y
        self.velocity_x = direction * LAUNCH_SPEED_X
        self.velocity_y = LAUNCH_SPEED_Y
        self.radius = 10.5 if ball_type == 1 else 20.5
        self.stopped = (direction == 0)  # direction 이 0이면 바닥에 놓인 공

    def update(self):
        if self.stopped:
            return
        dt = game_framework.frame_time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt - 0.5 * GRAVITY * dt ** 2
        self.velocity_y -= GRAVITY * dt
        # 화면 좌우 밖으로 나가면 제거 (바닥 처리는 잔디와의 충돌에서 한다)
        if self.x < -self.radius or self.x > get_canvas_width() + self.radius:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())  # 디버그용 충돌 박스
    
    def get_bb(self):
        return (self.x - self.radius, self.y - self.radius,
                self.x + self.radius, self.y + self.radius)

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            if self.stopped:  # 땅에 놓인 공만 주울 수 있다
                game_world.remove_object(self)
        elif group == 'grass:ball':
            if not self.stopped:  # 날아가던 공이 땅에 닿으면 땅 위에 멈춘다
                self.stopped = True
                self.y = other.get_bb()[3] + self.radius  # 잔디 윗면에 올려놓기
            
