import sys

import pygame
from pygame import Surface

from asset_manager import AssetType
from button import Button
from states.level_select_state import LevelSelectState
from states.state import State


class MenuState(State):
    _buttons: list[Button] = []
    
    def __init__(self):
        super().__init__()
        
        self._bg_image = pygame.image.load('assets/menu_bg.png')

    def prepare(self, game_manager, asset_manager):
        super().prepare(game_manager, asset_manager)

        self._buttons = [
            Button(rect=(100, 100, 250, 75),
                   click_event=self.go_to_level_select,
                   image=self._asset_manager.asset_dict[AssetType.PLAY_BUTTON].convert_alpha()),
            Button(rect=(100, 300, 250, 75),
                   image=self._asset_manager.asset_dict[AssetType.EXIT_BUTTON].convert_alpha(),
                   click_event=self.exit_game)
        ]

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