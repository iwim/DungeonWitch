# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

pygame.init()
background_colour = (255,255,255)
(width, height) = (1000, 500)
screen = pygame.display.set_mode((width, height))



screen.fill(background_colour)
pygame.display.set_caption("Dungeon Witch")
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
sys.exit()

