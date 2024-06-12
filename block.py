from abc import ABC
from dataclasses import dataclass

from enum import Enum
from pygame import image, Rect

@dataclass
class Block(ABC):
    """Represents a block in the game."""
    _img: image
    _rect: Rect
    _pushable: bool = False
    _is_solid: bool = False
    _is_destination: bool = False
    _z_index: int = 0

    def __init__(self, img: image, rect: Rect, pushable: bool, is_solid: bool, is_destination: bool = False, z_index: int = 0):
        """
        Initialize the Block with the given image, rectangle, pushability, solidity, destination status, and z-index.

        Args:
            img (image): The image of the block.
            rect (Rect): The rectangle representing the block's position and size.
            pushable (bool): A flag indicating whether the block can be pushed.
            is_solid (bool): A flag indicating whether the block is solid (not movable).
            is_destination (bool, optional): A flag indicating whether the block is a destination. Defaults to False.
            z_index (int, optional): The z-index of the block, used for drawing order. Defaults to 0.
        """
        self._img = img
        self._rect = rect
        self._pushable = pushable
        self._is_solid = is_solid
        self._is_destination = is_destination
        self._z_index = z_index

    @property
    def is_pushable(self) -> bool:
        """
        Check if the block is pushable.

        Returns:
            bool: True if the block is pushable, False otherwise.
        """
        return self._pushable

    @property
    def is_solid(self) -> bool:
        """
        Check if the block is solid.

        Returns:
            bool: True if the block is solid, False otherwise.
        """
        return self._is_solid

    @property
    def is_destination(self) -> bool:
        """
        Check if the block is a destination.

        Returns:
            bool: True if the block is a destination, False otherwise.
        """
        return self._is_destination

    @property
    def image(self) -> image:
        """
        Get the image of the block.

        Returns:
            image: The image of the block.
        """
        return self._img

    @image.setter
    def image(self, img: image):
        """
        Set the image of the block.

        Args:
            img (image): The new image of the block.
        """
        self._img = img

    @property
    def rect(self) -> Rect:
        """
        Get the rectangle of the block.

        Returns:
            Rect: The rectangle of the block.
        """
        return self._rect

    @property
    def z_index(self) -> int:
        """
        Get the z-index of the block.

        Returns:
            int: The z-index of the block.
        """
        return self._z_index