"""MacGiver Labyrinth Game
Game in which we have to move MacGyver to exite of the labyrinth.
He has to collect 3 iteams for syringe which could help to put the guard to sleep

Python script
Files: mg_labyrinthe.py, classes.py, constants.py + images"""

import math
import random

import pygame
from pygame.locals import * 

from classes import *
from constantes import *

    
pygame.init()

#Open the Pygame window
window = pygame.display.set_mode((x_size_window, y_size_window))
#Icon
game_icon = pygame.image.load(image_icon)
pygame.display.set_icon(game_icon)
#Name of the windoww
pygame.display.set_caption(name_window)
#Update window
pygame.display.flip()

field = Field()
tube = Iteams("tube", field.labyrinth)
needle = Iteams("needle", field.labyrinth)
ether = Iteams("ether", field.labyrinth)
mg = Hero(False, field.labyrinth)


tube.place_iteam()
field.update(tube.nl, tube.nc, mg.n_line, mg.n_column, "T")

needle.place_iteam()
field.update(needle.nl, needle.nc, mg.n_line, mg.n_column, "N")

ether.place_iteam()
field.update(ether.nl, ether.nc, mg.n_line, mg.n_column, "E")

field.update(mg.n_line, mg.n_column, mg.n_line, mg.n_column, "M")
field.affiche_lab(window)

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

    floor = pygame.image.load(image_floor).convert()
    guard = pygame.image.load(image_guard).convert_alpha()
    img_tube = pygame.image.load(image_tube).convert_alpha()
    img_needle = pygame.image.load(image_needle).convert_alpha()
    img_ether = pygame.image.load(image_ether).convert_alpha()
    img_mg = pygame.image.load(image_macgyver).convert_alpha()
    img_died = pygame.image.load(image_died).convert_alpha()
    img_escaped = pygame.image.load(image_escaped).convert_alpha()
    img_legend = pygame.image.load(image_legend).convert()

    if not mg.collect_tube:
        window.blit(img_tube, (tube.nc*size_sprite, tube.nl*size_sprite))
    if not mg.collect_ether:
        window.blit(img_ether, (ether.nc*size_sprite, ether.nl*size_sprite))
    if not mg.collect_needle:
        window.blit(img_needle, (needle.nc*size_sprite, needle.nl*size_sprite))
    
    window.blit(guard, (13*size_sprite, 14*size_sprite))
    window.blit(img_legend, (0, size_sprite*(y_number_sprites - 2)))
    window.blit(img_mg, (mg.n_column*size_sprite, mg.n_line*size_sprite))
    pygame.display.flip()

    mg.collect_iteams(tube, needle, ether)
    if mg.n_line == 14 and mg.n_column == 13:

        if mg.syringe == True:
            print("syringe is collected")
            print("MG is free")
            window.blit(img_escaped, (0, 0))
            pygame.display.flip()
            continuer_game = False 
            
        else:
            print("MG is dead")
            window.blit(img_died, (0, 0))
            pygame.display.flip()
            continuer_game = False 

    field.update(mg.n_line, mg.n_column, mg.n_line, mg.n_column, "M")
    field.affiche_lab(window)
    print("contue game", continuer_game, "\n", "iteams", mg.collect_needle, mg.collect_tube, mg.collect_ether, "syringe", mg.syringe)
    