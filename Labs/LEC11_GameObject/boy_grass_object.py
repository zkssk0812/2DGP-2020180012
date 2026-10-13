from pico2d import *
import random


# Game object class here

# 게임 객체를 파악
# boy, grass 가 필요하다

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        #self 자기 자신을 가리키는 더미변수
    def draw(self):
        self.image.draw(400, 30)
    def update(self): pass #통일성을 위해 형식적으로 만들어 주는 함수
    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(10, 300), 90
        self.frame = 0
        self.image = load_image('run_animation.png')
    
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += random.randint(5, 10)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

frame_w = 100
frame_h = 100

class Zombie:
    def __init__(self):
        self.x , self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += random.randint(1,10)
    def draw(self):
        self.image.clip_draw(self.frame * 430, 0 , 430, 519,
                             self.x, self.y, 430 // 2, 519 // 2)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global world

    world = []

    running = True
    #잔디 객체를 찍어낸다
    zombie = Zombie()
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(11)]
    world += team
    world.append(zombie)


def update_world():
    for object in world:
        object.update()
    pass

def render_world():
    clear_canvas()
    for object in world:
        object.draw()
    update_canvas()


open_canvas()

reset_world() #세상을 구정하는 객체들을 초기화

while running:
    handle_events()
    update_world()#객체들의 시물레이션 계산(game logic)
    render_world()#결과를 render
    delay(0.05)

close_canvas()

#객체를 찍어내는 도구
