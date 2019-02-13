#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MacGyver Labyrinth Game
Game in which we move MacGyver through a labyrinth
by collecting a syringe which would help him to put a guard to sleep
and exit from labyrinth.

Script Python
Files : dklabyrinthe.py, classes.py, constantes.py, l.txt + images
"""

import math
import random

import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

window = pygame.display.set_mode((x_size_window, y_size_window))
game_icon = pygame.image.load(image_icon)
pygame.display.set_icon(game_icon)
pygame.display.set_caption(name_window)

pygame.display.flip()

field = Field('l.txt')
mg = Hero(False, field.labyrinth)
tube = Iteams("tube", field.labyrinth)
needle = Iteams("needle", field.labyrinth)
ether = Iteams("ether", field.labyrinth)


tube.place_iteam()

needle.place_iteam()
while tube.y == needle.y and tube.x == needle.x:
    needle.place_iteam()

ether.place_iteam()
while (ether.y == needle.y and ether.x == needle.x) or\
        (ether.y == tube.y and ether.x == tube.x):
    ether.place_iteam()

field.display_lab(window)

continuer_game = True
while continuer_game:

    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer_game = 0

        elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer_game = 0
                elif event.key == K_RIGHT:
                    mg.move("R", field.labyrinth)
                elif event.key == K_LEFT:
                    mg.move("L", field.labyrinth)
                elif event.key == K_UP:
                    mg.move("U", field.labyrinth)
                elif event.key == K_DOWN:
                    mg.move("D", field.labyrinth)
                elif event.key == K_q:
                    continuer_game = 0
                    pygame.quit()
                    sys.exit()

    mg.show_iteams(tube, needle, ether)
    window.blit(mg.image_macgyver, (mg.x*sz_spr, mg.y*sz_spr))
    pygame.display.flip()
    mg.collect_iteams(tube, needle, ether)
    field.display_lab(window)
    if field.labyrinth[mg.y][mg.x] == "G":
        if mg.syringe is True:
            window.blit(mg.image_escaped, (0, 0))
            pygame.display.flip()
        else:
            window.blit(mg.image_died, (0, 0))
            pygame.display.flip()
        if mg.syringe is True:
            window.blit(mg.image_escaped, (0, 0))
            pygame.display.flip()
        else:
            window.blit(mg.image_died, (0, 0))
            pygame.display.flip()
