from abc import ABC, abstractmethod
from dataclasses import dataclass

from pygame import Surface

from asset_manager import AssetManager


@dataclass
class State(ABC):
    _game_manager: any
    asset_manager: AssetManager


    def __init__(self):
        self._game_manager = None


    def prepare(self, game_manager, asset_manager):
        self._game_manager = game_manager
        self.asset_manager = asset_manager


    @abstractmethod
    def update(self):
        ...


    @abstractmethod
    def draw(self, screen: Surface):
        ...
