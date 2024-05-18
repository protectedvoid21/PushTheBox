from abc import ABC, abstractmethod
from dataclasses import dataclass
from pygame import Surface


@dataclass
class State(ABC):
    _game_manager: any
    
    def prepare(self, game_manager):
        self._game_manager = game_manager
        
    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def draw(self, screen: Surface):
        ...