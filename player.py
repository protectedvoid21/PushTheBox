from dataclasses import dataclass

import pygame

from vector import Vector


@dataclass
class Player:
    _speed: int
    _position: Vector
    _image: pygame.image
    
    def __init__(self, image: pygame.image):
        self._image = image
    
    def move(self, direction: Vector):
        self._position += direction * self._speed
        
    def get_position(self) -> Vector:
        return self._position