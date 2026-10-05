from pico2d import *

open_canvas(800, 600)

Sheet = load_image('AnimationSheet.png')

walk = [
    (42, 998, 153, 178), 
    (244, 998, 153, 178), 
    (447, 997, 153, 179),
    (646, 997, 151, 179), 
    (843, 998, 152, 178), 
    (1033, 997, 153, 179),
]
run = [
    (38, 728, 237, 166), 
    (326, 734, 245, 160), 
    (618, 728, 250, 172), 
    (918, 730, 254, 167),
    (1221, 728, 240, 178), 
    (1520, 737, 242, 158), 
    (1814, 746, 240, 165), 
    (2108, 730, 238, 164),
]
jump = [
    (44, 434, 142, 163), 
    (243, 434, 141, 163), 
    (443, 440, 142, 164),
    (635, 428, 147, 169), 
    (830, 433, 141, 164),
]
attack =  [
    (44, 154, 143, 165), 
    (243, 154, 149, 165), 
    (441, 154, 149, 165), 
    (635, 154, 156, 161),
    (832, 153, 158, 159), 
    (1032, 153, 156, 161), 
    (1233, 148, 214, 238),
]

def Walking_Animation():
    for frame in walk:
        Draw_Character(frame)
        delay(0.033)
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


def Draw_Character(frame):
    left, bottom, w, h = frame
    clear_canvas()
    Sheet.clip_draw(left, bottom, w, h, 400, 300, w, h)
    update_canvas()
    pass


while True:
    Walking_Animation()
    Running_Animation()
    Jumping_Animation()
    Attack_Animation()
    pass