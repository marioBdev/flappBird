#pip install pygame
#if it needs upgrade pip =>python -m pip install --upgrade pip
import pygame
import os #library for address path in Python
import random

TELA_LARGURA=500
TELA_ALTURA = 800

PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','pipe.png')))
FLOOR_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','base.png')))
BKGROUNG_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bg.png')))
BIRD_IMAGE = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png')))
]

pygame.font.init()
POINTS_FONT = pygame,font.SysFont('arial',50)

class Bird:
    IMGS = BIRD-IMAGES
    # rotation animations
    MAX_ROTATION = 25
    ROTATION_SPEED = 20
    ANIMATION_TME = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.height = self.y
        self.time = 0
        self.image_counting = 0     #which image it'll be usig at the moment

    def jumping(self):
        self.speed = -10.05 # check it out how to test position movement
        self.time = 0

class Pipe:
    pass

class Floor:
    pass