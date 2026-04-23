import pygame
import os
import sys
import turtle

BULLET_IMAGE = pygame.image.load(os.path.join('img', 'bullet_image.png'))

class Game:

    def __init__(self,font, FPS, lives, window, screen_width, screen_height, bullets = 0, clock = pygame.time.Clock() ):
        self.font =font
        self.HEIGTH = screen_height
        self.WIDTH = screen_width
        self.FPS = FPS
        self.lives = lives
        self.level  = 1
        self.count = 0
        self.window = window
        self.clock = clock
        self.bullets = bullets #aqui
        self.bullet_img = BULLET_IMAGE
        registros = self.leer_registros("puntajes.txt")
        if len(registros) > 0:
            self.jugador, self.max_pun = registros[0] 
        else:
            self.max_pun = 0   

    def escape(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                return False
        