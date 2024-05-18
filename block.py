import abc
from dataclasses import dataclass
from pygame import image
from vector import Vector


@dataclass
class Block(abc.ABC):
    _img: image
    _position: Vector
    _pushable: bool = False
    _is_solid: bool = False
    
    def __init__(self, img: image, position: Vector):
        self._img = img
        self._position = position
        
    @property
    def image(self) -> image:
        return self._img
    
    @property
    def position(self) -> Vector:
        return self._position