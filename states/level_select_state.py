import pygame
from pygame import Surface

from button import Button
from states.in_game_state import InGameState
from level_loader import LevelLoader, LevelData
from states.state import State


class LevelSelectState(State):
    _level_loader: LevelLoader = LevelLoader()
    
    _buttons: list[Button] = []
    
    def __init__(self):
        super().__init__()
        self._buttons = [
            Button(pygame.Rect(100, 100, 250, 75), "Level 1", click_event=lambda: self.select_level(1), color=(255, 255, 255), font=pygame.font.Font(None, 20)),
            Button(pygame.Rect(100, 200, 250, 75), "Level 2", click_event=lambda: self.select_level(2), color=(255, 255, 255), font=pygame.font.Font(None, 20)),
            Button(pygame.Rect(100, 300, 250, 75), "Level 3", click_event=lambda: self.select_level(3), color=(255, 255, 255), font=pygame.font.Font(None, 20)),
            Button(pygame.Rect(100, 400, 250, 75), "Level 4", click_event=lambda: self.select_level(4), color=(255, 255, 255), font=pygame.font.Font(None, 20)),
            Button(pygame.Rect(100, 500, 250, 75), "Level 5", click_event=lambda: self.select_level(5), color=(255, 255, 255), font=pygame.font.Font(None, 20)),
        ]
    
    def select_level(self, level_name: int):
        level_data: LevelData = self._level_loader.load(level_name)
        
        self._game_manager.change_state(InGameState(level_data))
    
    def update(self):
        for button in self._buttons:
            button.update()

    def draw(self, screen: Surface):
        for button in self._buttons:
            button.draw(screen)