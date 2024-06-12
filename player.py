import math
from dataclasses import dataclass
from enum import Enum

import pygame
from pygame import Vector2

from camera import Camera
from constants import PLAYER_SPEED, PLAYER_ANIMATION_SPEED
from game_time import GameTime

class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'


@dataclass
class Player:
    """
    A class that represents the player in the game.
    
    The player has a speed, a rect, an image, animations, an animation index, an elapsed time, and a direction.
    
    The player can move, get the move direction, animate, and be drawn.
    """
    _speed: int
    _rect: pygame.Rect
    _image: pygame.image
    
    _animations: dict[Direction, list[pygame.image]]
    _animation_index: int = 0
    _elapsed_time: float = 0
    _direction: Direction = Direction.DOWN
    
    def __init__(self, image: pygame.image, initial_position: Vector2, animations: dict[Direction, list[pygame.image]]):
        """
        Initialize the Player with the given image, initial position, and animations.
    
        Args:
            image (pygame.image): The image of the player.
            initial_position (Vector2): The initial position of the player.
            animations (dict[Direction, list[pygame.image]]): The animations of the player.
        """
        self._image = image
        self._rect = self._image.get_rect()
        self._rect.center = initial_position + Vector2(self._rect.width / 2, self._rect.height / 2)
        self._speed = PLAYER_SPEED
        self._animations = animations
        

    def get_move_direction(self) -> Vector2:
        """
        Get the direction the player is trying to move.
    
        Returns:
            Vector2: The proposed player move direction.
        """
        keys = pygame.key.get_pressed()
        
        direction_vector = Vector2(0, 0)
        
        if keys[pygame.K_w]:
            direction_vector += Vector2(0, -1)
            self._direction = Direction.UP
        if keys[pygame.K_s]:
            direction_vector += Vector2(0, 1)
            self._direction = Direction.DOWN
        if keys[pygame.K_a]:
            direction_vector += Vector2(-1, 0)
            self._direction = Direction.LEFT
        if keys[pygame.K_d]:
            direction_vector += Vector2(1, 0)
            self._direction = Direction.RIGHT
            
        if direction_vector.length() == 0:
            self._animation_index = 0
            return Vector2(0, 0)
        
        self._animate()
        return direction_vector.normalize() * self._speed * GameTime.delta_time()
        
        
    def _animate(self):
        self._elapsed_time += GameTime.delta_time() * PLAYER_ANIMATION_SPEED
        self._animation_index = math.floor(self._elapsed_time % len(self._animations[self._direction]))
                        
        self._image = self._animations[self._direction][int(self._animation_index)]
        
    
    def move(self, direction: Vector2):
        """
        Move the player in the given direction.
    
        Args:
            direction (Vector2): The direction to move the player.
        """
        self._rect.move_ip(direction)
        
        
    @property
    def rect(self):
        """
        Get the rectangle representing the player's position and size.
        
        Returns:
            pygame.Rect: The rectangle representing the player's position and size.
        """
        return self._rect
    
    
    def draw(self, screen: pygame.Surface, camera: Camera):
        """
        Draw the player on the screen.

        Args:
            screen (pygame.Surface): The game screen.
            camera (Camera): The game camera.
        """
        screen.blit(self._image, camera.apply(self._rect))