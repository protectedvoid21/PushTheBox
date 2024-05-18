from abc import ABC, abstractmethod
from dataclasses import dataclass
from pygame import Surface


@dataclass
class State(ABC):
    _screen: Surface
    _game_manager: any
    
    def __init__(self, screen: Surface, game_manager):
        self._screen = screen
        self._game_manager = game_manager
        
    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def draw(self):
        ...