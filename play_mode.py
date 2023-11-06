import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy
    global balls

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    balls = [Ball(random.randint(100, 1600-100), 60, 0) for _ in range(50)]
    game_world.add_objects(balls, 1)

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # fill here
    for ball in balls.copy(): # 복사 안하면 위험한 접근 임..
        if game_world.collide(boy, ball):
            print('공과 소년이 부딪힘!')
            boy.ball_count += 1 # 소년 관점의 충돌 처리
            game_world.remove_object(ball) # 공을
            balls.remove(ball) # 제거

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

