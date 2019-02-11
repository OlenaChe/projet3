import math
import random

import pygame
from pygame.locals import * 
from constantes import *

window = pygame.display.set_mode((x_size_window, y_size_window))



class Field:
    

    def __init__(self, file):
        self.file = file
        self.labyrinth = []
        self.generer()
        self.guard = pygame.image.load(image_guard).convert()
        self.floor = pygame.image.load(image_floor).convert()
        self.legend = pygame.image.load(image_legend).convert()
    
    
    def generer(self):
        """""" 
        with open(self.file, "r") as file:
            structure_lab = []
            for line in file:
                line_lab = []
                for sprite in line:
                    if sprite != '\n':
                        line_lab.append(sprite)
                structure_lab.append(line_lab)
            self.labyrinth = structure_lab
    

    def affiche_lab(self, window):
        """ """

        num_line = 0
        for line in self.labyrinth:
            num_case = 0
            for sprite in line:
                x = num_case * 40
                y = num_line * 40
                if sprite != "1": 
                    if sprite == "G":
                        window.blit(self.guard, (x,y))
                    else:
                        window.blit(self.floor, (x,y))
                num_case += 1
            num_line += 1

        window.blit(self.legend, (0, size_sprite*(y_number_sprites - 2)))
        

    def update(self, nl, nc, letter):
        """ """
        self.labyrinth[nl][nc] = letter




class Iteams:
    """ """
    def __init__(self, name, labyrinth):
        """ """
        self.nl = 0
        self.nc = 0
        self.name = name
        self.labyrinth = labyrinth
    

    def place_iteam(self):
        """ """
        continue_place = 1
        while continue_place:
            nl = random.randrange(14)
            nc = random.randrange(14)

            if self.labyrinth[nl][nc] == "0":
                self.nl = nl
                self.nc = nc
                continue_place = 0
                print(self.name, "placement: ligne", self.nl + 1 , ", column", self.nc + 1)




class Hero:
    """Class Hero define a main character of game """
    def __init__(self, syringe, labyrinth):
        """ """
        self.image_macgyver = pygame.image.load(image_macgyver).convert_alpha()
        self.n_line = 0		# position № line
        self.n_column = 13 # position № column
        self.level = labyrinth
        self.syringe = False # hero has 3 iteams
        self.collect_tube = False
        self.collect_needle = False
        self.collect_ether = False
        self.img_tube = pygame.image.load(image_tube).convert_alpha()
        self.img_needle = pygame.image.load(image_needle).convert_alpha()
        self.img_ether = pygame.image.load(image_ether).convert_alpha()


    def collect_iteams(self, tube_, needle_, ether_):
        """ """
        if self.n_line == tube_.nl and self.n_column == tube_.nc:
            self.collect_tube = True
            print("tube is collected")
            window.blit(self.img_tube, (40, 600))
            pygame.display.flip()

        if self.n_line == needle_.nl and self.n_column == needle_.nc:
            self.collect_needle = True
            print("needle is collected")
            window.blit(self.img_needle, (80, 600))
            pygame.display.flip()

        if self.n_line == ether_.nl and self.n_column == ether_.nc:
            self.collect_ether = True
            print("ether is collected")
            window.blit(self.img_ether, (120, 600))
            pygame.display.flip()

        if (((self.collect_needle) and (self.collect_ether)) and (self.collect_tube)):
            self.syringe = True
        
        return(self.syringe)

    def show_iteams(self, tube_, needle_, ether_):
        if not self.collect_tube:
            window.blit(self.img_tube, (tube_.nc*size_sprite, tube_.nl*size_sprite))
        if not self.collect_ether:
            window.blit(self.img_ether, (ether_.nc*size_sprite, ether_.nl*size_sprite))
        if not self.collect_needle:
            window.blit(self.img_needle, (needle_.nc*size_sprite, needle_.nl*size_sprite))

    
    def move(self, direction, labyrinth):  
        """Determines the movement of the hero: right (R), left(L), up(U) and down(D)"""
        #move left
        window.blit(self.image_macgyver, (self.n_column*size_sprite, self.n_line*size_sprite))

        if direction == "L":
        
            if self.n_column > 0:
                
                if labyrinth[self.n_line][self.n_column - 1] != "1":
                    self.n_column -= 1
                    labyrinth[self.n_line][self.n_column] = "M"
                    labyrinth[self.n_line][self.n_column + 1] = "0"
                else:
                    print("STOP! This is a wall")

        #move right
        elif direction == "R":

            if self.n_column < 14:
                
                if labyrinth[self.n_line][self.n_column + 1] != "1":
                    self.n_column += 1
                    labyrinth[self.n_line][self.n_column] = "M"
                    labyrinth[self.n_line][self.n_column - 1] = "0"
                else:
                    print("STOP! This is a wall") 

        #move down
        elif direction == "D":

            if self.n_line < 14:
                
                if labyrinth[self.n_line + 1][self.n_column] != "1":
                    self.n_line += 1 
                    labyrinth[self.n_line][self.n_column] = "M"
                    labyrinth[self.n_line - 1][self.n_column] = "0"
                else:
                    print("STOP! This is a wall")

        #move up
        elif direction == "U":

            if self.n_line > 0:
                
                if labyrinth[self.n_line - 1][self.n_column] != "1":
                    self.n_line -= 1 
                    labyrinth[self.n_line][self.n_column] = "M"
                    labyrinth[self.n_line + 1][self.n_column] = "0"
                else:
                    print("STOP! This is a wall")

        #quit game
        elif direction == "Q":
            return False
        else:
            print("Input R (right) ou L (left) ou U (up) ou D (down) ou Q (quit)")


        print("You are here now: line №", self.n_line + 1,  ", column №", self.n_column + 1)

class Gardien:
    

    def __init__(self):
        
        self.guard = pygame.image.load(image_guard).convert()


    def show(self):
        num_line = 0
        for line in self.labyrinth:
            num_case = 0
            for sprite in line:
                x = num_case * 40
                y = num_line * 40
                if sprite == "G":         
                    window.blit(self.guard, (x,y))
                num_case += 1
            num_line += 1



