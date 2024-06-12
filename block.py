from abc import ABC
from dataclasses import dataclass

from enum import Enum
from pygame import image, Rect


@dataclass
class Block(ABC):
    _img: image
    _rect: Rect
    _pushable: bool = False
    _is_solid: bool = False
    _is_destination: bool = False
    _z_index: int = 0


    def __init__(self, img: image, rect: Rect, pushable: bool, is_solid: bool, is_destination: bool = False,
                 z_index: int = 0):
        self._img = img
        self._rect = rect
        self._pushable = pushable
        self._is_solid = is_solid
        self._is_destination = is_destination
        self._z_index = z_index


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


    @image.setter
    def image(self, img: image):
        self._img = img


    @property
    def rect(self) -> Rect:
        return self._rect


    @property
    def z_index(self) -> int:
        return self._z_index
