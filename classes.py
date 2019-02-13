import math
import random

import pygame
from pygame.locals import *
from constantes import *

window = pygame.display.set_mode((x_size_window, y_size_window))


class Field:
    """ """
    def __init__(self, file):
        self.file = file
        self.labyrinth = []
        self.generate()
        self.guardian = pygame.image.load(image_guardian).convert_alpha()
        self.floor = pygame.image.load(image_floor).convert()
        self.legend = pygame.image.load(image_legend).convert()

    def generate(self):
        """ """
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
        """ """
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
        window.blit(self.legend, (0, sz_spr*(y_number_sprites - 2)))


class Iteams:
    """ """
    def __init__(self, name, labyrinth):
        """ """
        self.y = 0
        self.x = 0
        self.name = name
        self.labyrinth = labyrinth

    def place_iteam(self):
        """ """
        continue_place = 1
        while continue_place:
            y = random.randrange(14)
            x = random.randrange(14)

            if self.labyrinth[y][x] == "0":
                self.y = y
                self.x = x
                continue_place = 0


class Hero:
    """Class Hero define a main character of game """
    def __init__(self, syringe, labyrinth):
        """ """
        self.image_macgyver = pygame.image.load(image_macgyver).convert_alpha()
        self.y = mg_y
        self.x = mg_x
        self.level = labyrinth
        self.syringe = False
        self.collect_tube = False
        self.collect_needle = False
        self.collect_ether = False
        self.image_tube = pygame.image.load(image_tube).convert_alpha()
        self.image_needle = pygame.image.load(image_needle).convert_alpha()
        self.image_ether = pygame.image.load(image_ether).convert_alpha()
        self.image_died = pygame.image.load(image_died).convert_alpha()
        self.image_escaped = pygame.image.load(image_escaped).convert_alpha()

    def collect_iteams(self, tube, needle, ether):
        """ """
        if self.y == tube.y and self.x == tube.x:
            self.collect_tube = True
            window.blit(self.image_tube, (40, 600))
            pygame.display.flip()
        if self.y == needle.y and self.x == needle.x:
            self.collect_needle = True
            window.blit(self.image_needle, (80, 600))
            pygame.display.flip()
        if self.y == ether.y and self.x == ether.x:
            self.collect_ether = True
            window.blit(self.image_ether, (120, 600))
            pygame.display.flip()
        if self.collect_needle and self.collect_ether and self.collect_tube:
            self.syringe = True
        return(self.syringe)

    def show_iteams(self, tube, needle, ether):
        if not self.collect_tube:
            window.blit(self.image_tube, (tube.x*sz_spr, tube.y*sz_spr))
        if not self.collect_ether:
            window.blit(self.image_ether, (ether.x*sz_spr, ether.y*sz_spr))
        if not self.collect_needle:
            window.blit(self.image_needle, (needle.x*sz_spr, needle.y*sz_spr))

    def move(self, direction, labyrinth):
        """Determines the movement of the hero:
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
    """"""
    def __init__(self):
        self.guardian = pygame.image.load(image_guardian).convert()

    def show_guardian(self):
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
