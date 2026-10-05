from pico2d import *

open_canvas(800, 600)

Sheet = load_image('AnimationSheet.png')

def Walking_Animation():
    print('Walking')
    pass


def Running_Animation():
    print('Running')
    pass


def Jumping_Animation():
    print('Jumping')
    pass


def Attack_Animation():
    print('Attack')
    pass


def Draw_Character():
    pass


while True:

    clear_canvas()
    Sheet.draw(400, 300)
    update_canvas()
    delay(0.01)

    Walking_Animation()
    Running_Animation()
    Jumping_Animation()
    Attack_Animation()
    pass