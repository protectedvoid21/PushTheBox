from dataclasses import dataclass

import pygame
from pygame import Vector2

from constants import PLAYER_SPEED
from game_time import GameTime


@dataclass
class Player:
    _speed: int
    _rect: pygame.Rect
    _image: pygame.image
    
    def __init__(self, image: pygame.image, initial_position: Vector2):
        self._image = image
        self._rect = self._image.get_rect()
        self._rect.center = initial_position + Vector2(self._rect.width // 2, self._rect.height // 2)
        self._speed = PLAYER_SPEED
        

    def get_move_direction(self) -> Vector2:
        keys = pygame.key.get_pressed()
        
        direction = Vector2(0, 0)
        
        if keys[pygame.K_w]:
            direction += Vector2(0, -1)
        if keys[pygame.K_s]:
            direction += Vector2(0, 1)
        if keys[pygame.K_a]:
            direction += Vector2(-1, 0)
        if keys[pygame.K_d]:
            direction += Vector2(1, 0)
            
        if direction.length() > 0:
            return direction.normalize() * self._speed * GameTime.delta_time()
        
        return Vector2(0, 0)
        
    
    def move(self, direction: Vector2):
        self._rect.move_ip(direction)
        
        
    @property
    def rect(self):
        return self._rect
    
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self._image, self._rect)