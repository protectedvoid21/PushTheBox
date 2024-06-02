import sys

import pygame
from pygame import Surface

from button import Button
from states.level_select_state import LevelSelectState
from states.state import State


class MenuState(State):
    _buttons: list[Button] = []
    
    def __init__(self):
        super().__init__()
        self._buttons = [
            Button((100, 100, 250, 75), "Play", font=pygame.font.Font(None, 20), color=(255, 255, 255), click_event=self.go_to_level_select),
            Button((100, 300, 250, 75), "Exit", font=pygame.font.Font(None, 20), color=(255, 255, 255), click_event=self.exit_game)
        ]
        
        self._bg_image = pygame.image.load('assets/menu_bg.png')

    def go_to_level_select(self):
        self._game_manager.change_state(LevelSelectState())
    
    def exit_game(self):
        sys.exit(0)

    def update(self):
        for button in self._buttons:
            button.update()

    def draw(self, screen: Surface):
        self._bg_image = pygame.transform.scale(self._bg_image, (screen.get_width(), screen.get_height()))
        screen.blit(self._bg_image, (0, 0))
        
        for button in self._buttons:
            button.draw(screen)