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
mg = Hero(False, field.labyrinth)
tube = Iteams("tube", field.labyrinth)
needle = Iteams("needle", field.labyrinth)
ether = Iteams("ether", field.labyrinth)


tube.place_iteam()
#field.update(tube.nl, tube.nc, "T")
needle.place_iteam()
while tube.nl == needle.nl and tube.nc == needle.nc:
    needle.place_iteam()
#field.update(needle.nl, needle.nc, "N")

ether.place_iteam()
while (ether.nl == needle.nl and ether.nc == needle.nc) or (ether.nl == tube.nl and ether.nc == tube.nc):
    ether.place_iteam()
#field.update(ether.nl, ether.nc, "E")

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
    window.blit(mg.image_macgyver, (mg.n_column*size_sprite, mg.n_line*size_sprite))
    pygame.display.flip()

    mg.collect_iteams(tube, needle, ether)
  
    if field.labyrinth[mg.n_line][mg.n_column] == "G":
        if mg.syringe == True:
            window.blit(mg.img_escaped, (0, 0))
            pygame.display.flip()  

        else:
            window.blit(mg.img_died, (0, 0))
            pygame.display.flip()


        if mg.syringe == True:
            window.blit(mg.img_escaped, (0, 0))
            pygame.display.flip()  
            
        else:
            window.blit(mg.img_died, (0, 0))
            pygame.display.flip()
           
    field.display_lab(window)