from abc import ABC
from dataclasses import dataclass

from pygame import image, Rect


@dataclass
class Block(ABC):
    _img: image
    _rect: Rect
    _pushable: bool = False
    _is_solid: bool = False
    _is_destination: bool = False
    
    def __init__(self, img: image, rect: Rect, pushable: bool, is_solid: bool, is_destination: bool = False):
        self._img = img
        self._rect = rect
        self._pushable = pushable
        self._is_solid = is_solid
        self._is_destination = is_destination
        
        
    @property
    def is_pushable(self) -> bool:
        return self._pushable
    
    @property
    def is_solid(self) -> bool:
        return self._is_solid
    
    @property
    def is_destination(self) -> bool:
        return self._is_destination
    
    @property
    def image(self) -> image:
        return self._img
            
    @property
    def rect(self) -> Rect:
        return self._rect