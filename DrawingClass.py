import pygame
import os
from EnemyClass import Enemy
from ShipClass import Ship
from GameClass import Game
from BulletClass import Bullet

current_dir = os.path.dirname(__file__)
BACKGROUND = pygame.image.load(os.path.join('img', 'background.png'))
WIDTH, HEIGTH = 800, 600
class Drawing:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.SysFont('comicsans', 50)
      
    def drawing(self, game, player, enemies, FPS, puntos):
        # Drawing the background
        self.window.blit(BACKGROUND, (0,0))
        player.fire(self.window)


        # Drawing the enemies
        # We made a copy of the enemy list to avoid bugs because we are removing from the list at the same time that we are iterating on it
        for enemy in enemies[:]:
            enemy.draw(self.window)
        
        player.draw(self.window)

        # Drawing the HUD
        game.draw_HUD()
        points_label = self.font.render(f'Puntos: {puntos}', 1, (255,255,255))
        self.window.blit(points_label,(HEIGTH/2,10))
        pygame.display.update()




