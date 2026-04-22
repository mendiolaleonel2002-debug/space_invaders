import pygame
import os
from ShipClass import Ship
from EnemyClass import Enemy
from BulletClass import Bullet

# Definir otras constantes relacionadas con el juego
PLAYER_IMAGE = pygame.image.load(os.path.join('img', 'player_image.png'))
BULLET_IMAGE = pygame.image.load(os.path.join('img', 'bullet_image.png'))

# Clase player

class Player(Ship):
    def __init__(self, x, y, x_speed, y_speed, health=100):
        super().__init__(x, y, health)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.ship_img = PLAYER_IMAGE
        self.bullet_img = BULLET_IMAGE
        self.bullet_speed = -10
        self.max_health = health
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.creation_cooldown_counter = 0
        self.max_amount_bullets = 3
        
        
        
        
    