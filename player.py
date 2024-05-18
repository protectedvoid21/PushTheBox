from dataclasses import dataclass

import pygame

from game_time import GameTime
from vector import Vector


@dataclass
class Player:
    _speed: int
    _position: Vector
    _image: pygame.image
    
    def __init__(self, image: pygame.image, initial_position: Vector = Vector(0, 0), speed: int = 1):
        self._image = image
        self._position = initial_position
        self._speed = speed
        

    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        direction = Vector(0, 0)
        
        if keys[pygame.K_w]:
            direction += Vector(0, -1)
        if keys[pygame.K_s]:
            direction += Vector(0, 1)
        if keys[pygame.K_a]:
            direction += Vector(-1, 0)
        if keys[pygame.K_d]:
            direction += Vector(1, 0)
            
        self._move(direction)
        
    
    def _move(self, direction: Vector):
        self._position += direction * self._speed * GameTime.delta_time
        
        
    def get_position(self) -> Vector:
        return self._position
    
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self._image, self._position.get_tuple())