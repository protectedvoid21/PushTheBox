from dataclasses import dataclass

import pygame

from block import Block
from vector import Vector


@dataclass
class BlockWall(Block):
    _image: pygame.image
    _position: Vector
    
    def __init__(self, position: Vector):
        super().__init__(position)
        self.image = pygame.image.load("wall.png")