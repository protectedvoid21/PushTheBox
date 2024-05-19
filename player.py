import math
from dataclasses import dataclass
from enum import Enum

import pygame
from pygame import Vector2

from constants import PLAYER_SPEED
from game_time import GameTime

class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'


@dataclass
class Player:
    _speed: int
    _rect: pygame.Rect
    _image: pygame.image
    
    _animations: dict[Direction, list[pygame.image]]
    _animation_index: int = 0
    _elapsed_time: float = 0
    _animation_speed: float = 5
    _direction: Direction = Direction.DOWN
    
    def __init__(self, image: pygame.image, initial_position: Vector2, animations: dict[Direction, list[pygame.image]]):
        self._image = image
        self._rect = self._image.get_rect()
        self._rect.center = initial_position + Vector2(self._rect.width / 2, self._rect.height / 2)
        self._speed = PLAYER_SPEED
        self._animations = animations
        

    def get_move_direction(self) -> Vector2:
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
        self._elapsed_time += GameTime.delta_time() * self._animation_speed
        self._animation_index = math.floor(self._elapsed_time % len(self._animations[self._direction]))
                        
        self._image = self._animations[self._direction][int(self._animation_index)]
        
    
    def move(self, direction: Vector2):
        self._rect.move_ip(direction)
        
        
    @property
    def rect(self):
        return self._rect
    
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self._image, self._rect)