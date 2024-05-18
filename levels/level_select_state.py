from pygame import Surface

from in_game_state import InGameState
from levels.level_loader import LevelLoader
from state import State


class LevelSelectState(State):
    _level_loader: LevelLoader = LevelLoader()
    
    def __init__(self, screen, game_manager):
        super().__init__(screen, game_manager)
        
    
    def select_level(self, level_name):
        blocks = self._level_loader.load(level_name)
        
        self._game_manager.change_state(InGameState(), blocks)
    
    def update(self):
        pass

    def draw(self, screen: Surface):
        pass