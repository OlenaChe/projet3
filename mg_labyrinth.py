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

pygame.display.flip()

field = Field('l.txt')
print(field.labyrinth)
tube = Iteams("tube", field.labyrinth)
needle = Iteams("needle", field.labyrinth)
ether = Iteams("ether", field.labyrinth)
mg = Hero(False, field.labyrinth)


tube.place_iteam()
field.update(tube.nl, tube.nc, "T")

needle.place_iteam()
field.update(needle.nl, needle.nc, "N")

ether.place_iteam()
field.update(ether.nl, ether.nc, "E")

field.update(mg.n_line, mg.n_column, "M")
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
                elif event.key == K_q:
                    continuer_game = 0 
                    pygame.quit()
                    sys.exit()

    mg.show_iteams(tube, needle, ether)
    img_died = pygame.image.load(image_died).convert_alpha()
    img_escaped = pygame.image.load(image_escaped).convert_alpha()
    img_legend = pygame.image.load(image_legend).convert()

    
    
    
    
    pygame.display.flip()

    mg.collect_iteams(tube, needle, ether)
    if mg.n_line == 14 and mg.n_column == 13:

        if mg.syringe == True:
            print("syringe is collected")
            print("MG is free")
            window.blit(img_escaped, (0, 0))
            pygame.display.flip()
            #continuer_game = False 
            
        else:
            print("MG is dead")
            window.blit(img_died, (0, 0))
            pygame.display.flip()
            #continuer_game = False 

    field.update(mg.n_line, mg.n_column, "M")
    field.affiche_lab(window)
    print("contue game", continuer_game, "\n", "iteams", mg.collect_needle, mg.collect_tube, mg.collect_ether, "syringe", mg.syringe)
    