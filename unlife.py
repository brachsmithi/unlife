import pygame
import random
from pygame.locals import *
from sys import exit
from field_tracker import FieldTracker
from human import Human
from monster import Monster
from mover import Mover
from random_motion_generator import RandomMotionGenerator

screen_width = 600
screen_height = 400
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

field_tracker = FieldTracker()
# TODO: Need to disallow duplicate placement in initial load!
for i in range(0, 100):
    human = Human(random.randint(0, screen_width), random.randint(0, screen_height))
    field_tracker.add_human(human)
field_tracker.add_monster(Monster(random.randint(0, screen_width), random.randint(0, screen_height)))
mover = Mover(RandomMotionGenerator(), screen_width, screen_height)

while True:

    shut_down = False
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            shut_down = True

    if shut_down:
        break

    screen.fill((0, 0, 0))
    new_tracker = FieldTracker()
    for human in field_tracker.humans:
        mover.move(human, new_tracker)
        screen.set_at(human.position(), (50, 205, 50))
    for monster in field_tracker.monsters:
        mover.move(monster, new_tracker)
        screen.set_at(human.position(), (255, 0, 0))
    field_tracker = new_tracker
    
    pygame.display.update()
    clock.tick(30)
