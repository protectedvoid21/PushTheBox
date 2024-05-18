import time
from dataclasses import dataclass

import pygame.time


@dataclass
class GameTime:
    _framerate: int
    _clock = pygame.time.Clock()
    _previous_time: float = time.time()
    _delta_time = 0.0
    

    def __init__(self, framerate):
        self._framerate = framerate
        
    def update(self):
        self._clock.tick(self._framerate)
        now = time.time()
        self._delta_time = now - self._previous_time
        self._previous_time = now
    
    
    @classmethod
    def delta_time(cls) -> float:
        return cls._delta_time
