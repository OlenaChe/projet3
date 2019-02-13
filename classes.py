"""MacGyver Labyrunth Game Classes"""

import math
import random

import pygame
from pygame.locals import *
from constantes import *

window = pygame.display.set_mode((X_SIZE_WINDOW, Y_SIZE_WINDOW))


class Field:
    """Classe which creates a field of the game"""
    def __init__(self, file):
        self.file = file
        self.labyrinth = []
        self.generate()
        self.guardian = pygame.image.load(IMAGE_GUARDIAN).convert_alpha()
        self.floor = pygame.image.load(IMAGE_FLOOR).convert()
        self.legend = pygame.image.load(IMAGE_LEGEND).convert()

    def generate(self):
        """Method for generating the field structure based on the file.
        We create a list which contains other lists consisting of lines"""
        with open(self.file, "r") as file:
            structure_lab = []
            for line in file:
                line_lab = []
                for sprite in line:
                    if sprite != '\n':
                        line_lab.append(sprite)
                structure_lab.append(line_lab)
            self.labyrinth = structure_lab

    def display_lab(self, window):
        """Method for displaying a labyrinth"""
        num_line = 0
        for line in self.labyrinth:
            num_case = 0
            for sprite in line:
                y = num_line * 40
                x = num_case * 40
                if sprite != "1":
                    if sprite == "G":
                        window.blit(self.floor, (x, y))
                        window.blit(self.guardian, (x, y))
                    else:
                        window.blit(self.floor, (x, y))
                num_case += 1
            num_line += 1
        window.blit(self.legend, (0, SZ_SPR*(Y_NUMBER_SPRITES - 2)))


class Iteams:
    """Classe defines the iteams which has to be collected by game character"""
    def __init__(self, name, labyrinth):
        self.y = 0
        self.x = 0
        self.name = name
        self.labyrinth = labyrinth

    def place_iteam(self):
        """Method allows to place the iteams in random order"""
        continue_place = 1
        while continue_place:
            y = random.randrange(14)
            x = random.randrange(14)

            if self.labyrinth[y][x] == "0":
                self.y = y
                self.x = x
                continue_place = 0


class Hero:
    """Class defines a character of game"""
    def __init__(self, labyrinth):
        self.IMAGE_MACGYVER = pygame.image.load(IMAGE_MACGYVER).convert_alpha()
        self.y = MG_Y
        self.x = MG_X
        self.level = labyrinth
        self.syringe = False
        self.collect_tube = False
        self.collect_needle = False
        self.collect_ether = False
        self.IMAGE_TUBE = pygame.image.load(IMAGE_TUBE).convert_alpha()
        self.IMAGE_NEEDLE = pygame.image.load(IMAGE_NEEDLE).convert_alpha()
        self.IMAGE_ETHER = pygame.image.load(IMAGE_ETHER).convert_alpha()
        self.IMAGE_DIED = pygame.image.load(IMAGE_DIED).convert_alpha()
        self.IMAGE_ESCAPED = pygame.image.load(IMAGE_ESCAPED).convert_alpha()

    def collect_iteams(self, tube, needle, ether):
        """Methode defines and show board below which iteams are collected
        and whether the syringe is ready"""
        if self.y == tube.y and self.x == tube.x:
            self.collect_tube = True
            window.blit(self.IMAGE_TUBE, (40, 600))
            pygame.display.flip()
        if self.y == needle.y and self.x == needle.x:
            self.collect_needle = True
            window.blit(self.IMAGE_NEEDLE, (80, 600))
            pygame.display.flip()
        if self.y == ether.y and self.x == ether.x:
            self.collect_ether = True
            window.blit(self.IMAGE_ETHER, (120, 600))
            pygame.display.flip()
        if self.collect_needle and self.collect_ether and self.collect_tube:
            self.syringe = True

    def show_iteams(self, tube, needle, ether):
        """Methode displays the iteams on the field
        until they are not collected"""
        if not self.collect_tube:
            window.blit(self.IMAGE_TUBE, (tube.x*SZ_SPR, tube.y*SZ_SPR))
        if not self.collect_ether:
            window.blit(self.IMAGE_ETHER, (ether.x*SZ_SPR, ether.y*SZ_SPR))
        if not self.collect_needle:
            window.blit(self.IMAGE_NEEDLE, (needle.x*SZ_SPR, needle.y*SZ_SPR))

    def move(self, direction, labyrinth):
        """Methode determines the movement of the hero:
        right (R), left(L), up(U) and down(D)"""
        if direction == "L":
            if self.x > 0:
                if labyrinth[self.y][self.x - 1] != "1":
                    self.x -= 1
                    labyrinth[self.y][self.x + 1] = "0"
        elif direction == "R":
            if self.x < 14:
                if labyrinth[self.y][self.x + 1] != "1":
                    self.x += 1
                    labyrinth[self.y][self.x - 1] = "0"
        elif direction == "D":
            if self.y < 14:
                if labyrinth[self.y + 1][self.x] != "1":
                    self.y += 1
                    labyrinth[self.y - 1][self.x] = "0"
        elif direction == "U":
            if self.y > 0:
                if labyrinth[self.y - 1][self.x] != "1":
                    self.y -= 1
                    labyrinth[self.y + 1][self.x] = "0"


class Guardian:
    """Class defines an antagonist who guards the exit"""
    def __init__(self):
        self.guardian = pygame.image.load(IMAGE_GUARDIAN).convert()

    def show_guardian(self):
        """Methode displays an image of the guardian
        according to his sprite coordinates"""
        num_line = 0
        for line in self.labyrinth:
            num_case = 0
            for sprite in line:
                y = num_line * 40
                x = num_case * 40
                if sprite == "G":
                    window.blit(self.guardian, (x, y))
                num_case += 1
            num_line += 1
