from dataclasses import dataclass
from pygame import image
from vector import Vector


@dataclass
class Block:
    _img: image
    _position: Vector
    
    def __init__(self, img: image, position: Vector):
        self._img = img
        self._position = position