import abc
from dataclasses import dataclass

from pygame import image, Vector2


@dataclass
class Block(abc.ABC):
    _img: image
    _position: Vector2
    _pushable: bool = False
    _is_solid: bool = False
    
    def __init__(self, img: image, position: Vector2):
        self._img = img
        self._position = position
        
    @property
    def image(self) -> image:
        return self._img
    
    @property
    def position(self) -> Vector2:
        return self._position