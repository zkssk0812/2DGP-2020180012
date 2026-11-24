from pico2d import *
import game_world

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.ruler_image = load_image('ruler.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        self.ruler_image.draw(800, 350)
        draw_rectangle(*self.get_bb())  # 디버그용 충돌 박스

    def get_bb(self):
        return 0, 0, 1600, 60

    def handle_collision(self, group, other):
        pass  # 공이 땅에 닿았을 때의 처리는 Ball 쪽에서 한다


