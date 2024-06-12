import time
from dataclasses import dataclass

import pygame.time


@dataclass
class GameTime:
    """
        A class that manages the game time.
        
        This class is a singleton and should not be instantiated.
        
        To get the delta time, use GameTime.delta_time().
    """
    _framerate: int
    _clock = pygame.time.Clock()
    _previous_time: float = time.time()
    _delta_time = 0.0
    

    def __init__(self, framerate):
        """
            Initialize the GameTime with the given framerate.
    
            Args:
                framerate (int): The framerate of the game.
        """
        self._framerate = framerate
        
    def update(self):
        """
            Update the game time.

            This method should be called once per frame. It updates the delta time and sets the previous time to the current time.
        """
        self._clock.tick(self._framerate)
        now = time.time()
        GameTime._delta_time = now - self._previous_time
        self._previous_time = now
    
    
    @classmethod
    def delta_time(cls) -> float:
        """
            Get elapsed time since the last frame.
            
            Use it for making movements frame-rate independent.
                        
            Returns:
                float: The time since the last frame.
        """
        return cls._delta_time
