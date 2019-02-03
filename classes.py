"""MacGyver Game Classes"""

import math
import random

import pygame
from pygame.locals import * 
from constantes import *

#Opening the Pygame window
window = pygame.display.set_mode((x_size_window, y_size_window))
# Loading images
img_tube = pygame.image.load(image_tube).convert_alpha()
img_needle = pygame.image.load(image_needle).convert_alpha()
img_ether = pygame.image.load(image_ether).convert_alpha()
img_legend = pygame.image.load(image_legend).convert_alpha()


class Field:
    """Class which defines a labyrinth"""
    def __init__(self):
        """Method which creates a labyrinth"""
        self.labyrinth = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1,1,1,1],
        [1,0,1,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,1,0,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,1,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,0,0,0,0,0,0,1,0,1],
        [1,0,0,0,1,1,1,1,0,1,1,1,1,1,1],
        [1,1,1,0,1,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,0,0,0,1,1,0,0,0,0,0,1],
        [1,0,1,1,1,1,0,0,1,1,1,1,1,1,1],
        [1,0,1,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,0,1,1,1,1,1,1,1,0,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,"G",1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
    

    def affiche_lab(self, window):
        """Methode which displays a labyrinth"""
        for line in self.labyrinth:
            print(" ".join([str(x) for x in line]))
        # Loading images
        floor = pygame.image.load(image_floor).convert()
        guard = pygame.image.load(image_guard).convert_alpha()
        tube = pygame.image.load(image_tube).convert_alpha()
        needle = pygame.image.load(image_needle).convert_alpha()
        ether = pygame.image.load(image_ether).convert_alpha()
        legend = pygame.image.load(image_legend).convert()

        num_line = 0
        for line in self.labyrinth:
            num_case = 0
            for sprite in line:
                x = num_case * 40
                y = num_line * 40
                if sprite != 1:         
                    window.blit(floor, (x,y))
                num_case += 1
            num_line += 1


    def update(self, nl, nc, n_line, n_column, letter):
        """Methode which updates the labyrinth"""
        self.labyrinth[nl][nc] = letter




class Iteams:
    """Class defines the iteams of syringe which MacGyver has to collect"""
    def __init__(self, name, labyrinth):
        """Methode which creates the iteams"""
        self.nl = 0
        self.nc = 0
        self.name = name
        self.labyrinth = labyrinth
    

    def place_iteam(self):
        """Methode which places the iteams in labyrinth"""
        continue_place = 1
        while continue_place:
            nl = random.randrange(14)
            nc = random.randrange(14)

            if self.labyrinth[nl][nc] == 0:
                self.nl = nl
                self.nc = nc
                continue_place = 0
                print(self.name, "placement: ligne", self.nl + 1 , ", column", self.nc + 1)




class Hero:
    """Class Hero which defines a main character of the game"""
    def __init__(self, syringe, labyrinth):
        """Methode which creates a a main character"""
        self.image_macgyver = pygame.image.load(image_macgyver).convert_alpha()
        self.n_line = 0		# position № line
        self.n_column = 13 # position № column
        self.level = labyrinth
        self.syringe = False # hero has 3 iteams
        self.collect_tube = False
        self.collect_needle = False
        self.collect_ether = False


    def collect_iteams(self, tube_, needle_, ether_):
        """ 
        if self.n_line == tube_.nl and self.n_column == tube_.nc:
            self.collect_tube = True
            print("tube is collected")
            window.blit(img_tube, (40, 600))
            pygame.display.flip()

        if self.n_line == needle_.nl and self.n_column == needle_.nc:
            self.collect_needle = True
            print("needle is collected")
            window.blit(img_needle, (80, 600))
            pygame.display.flip()

        if self.n_line == ether_.nl and self.n_column == ether_.nc:
            self.collect_ether = True
            print("ether is collected")
            window.blit(img_ether, (120, 600))
            pygame.display.flip()

        if (((self.collect_needle) and (self.collect_ether)) and (self.collect_tube)):
            self.syringe = True
        
        return(self.syringe)

    
    def move(self, direction, labyrinth):  
        """Methode which determines the movement of the hero: 
        right (R), left(L), up(U) and down(D)"""
        #move left
        if direction == "L":
        
            if self.n_column > 0:
                
                if labyrinth[self.n_line][self.n_column - 1] != 1:
                    self.n_column -= 1
                    labyrinth[self.n_line][self.n_column] = "M"
                    labyrinth[self.n_line][self.n_column + 1] = 0
                else:
                    print("STOP! This is a wall")

        #move right
        elif direction == "R":

            if self.n_column < 14:
                
                if labyrinth[self.n_line][self.n_column + 1] != 1:
                    self.n_column += 1
                    labyrinth[self.n_line][self.n_column] = "M"
                    labyrinth[self.n_line][self.n_column - 1] = 0
                else:
                    print("STOP! This is a wall") 

        #move down
        elif direction == "D":

            if self.n_line < 14:
                
                if labyrinth[self.n_line + 1][self.n_column] != 1:
                    self.n_line += 1 
                    labyrinth[self.n_line][self.n_column] = "M"
                    labyrinth[self.n_line - 1][self.n_column] = 0
                else:
                    print("STOP! This is a wall")

        #move up
        elif direction == "U":

            if self.n_line > 0:
                
                if labyrinth[self.n_line - 1][self.n_column] != 1:
                    self.n_line -= 1 
                    labyrinth[self.n_line][self.n_column] = "M"
                    labyrinth[self.n_line + 1][self.n_column] = 0
                else:
                    print("STOP! This is a wall")

        #quit game
        elif direction == "Q":
            return False
        else:
            print("Input R (right) ou L (left) ou U (up) ou D (down) ou Q (quit)")


        print("You are here now: line №", self.n_line + 1,  ", column №", self.n_column + 1)
