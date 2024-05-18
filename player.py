from dataclasses import dataclass

import pygame
from pygame import Vector2

from constants import PLAYER_SPEED
from game_time import GameTime


@dataclass
class Player:
    _speed: int
    _position: Vector2
    _image: pygame.image
    
    def __init__(self, image: pygame.image, initial_position: Vector2):
        self._image = image
        self._position = initial_position
        self._speed = PLAYER_SPEED
        

    def handle_input(self):
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
            self._move(direction.normalize())
        
    
    def _move(self, direction: Vector2):
        self._position += direction * self._speed * GameTime.delta_time()
        
        
    def get_position(self) -> Vector2:
        return self._position
    
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self._image, self._position)