import sys

import pygame
from pygame import Surface

from asset_manager import AssetType, AssetManager
from button import Button
from states.level_select_state import LevelSelectState
from states.state import State


class MenuState(State):
    _buttons: list[Button] = []
    _bg_image: Surface


    def __init__(self):
        super().__init__()


    def prepare(self, game_manager, asset_manager):
        super().prepare(game_manager, asset_manager)

        self._bg_image = self.asset_manager[AssetType.MENU_BACKGROUND]
        self._bg_image = pygame.transform.scale(self._bg_image, (
        pygame.display.get_window_size()[0], pygame.display.get_window_size()[1]))

        self._buttons = [
            Button(rect=(100, 100, 250, 75),
                   font=self.asset_manager.default_font,
                   text='Play',
                   click_event=self.go_to_level_select,
                   image=self.asset_manager[AssetType.GREEN_BUTTON].convert_alpha()),
            Button(rect=(100, 300, 250, 75),
                   font=self.asset_manager.default_font,
                   text='Exit',
                   click_event=self.exit_game,
                   image=self.asset_manager[AssetType.RED_BUTTON].convert_alpha())
        ]


    def go_to_level_select(self):
        self._game_manager.change_state(LevelSelectState())


    def exit_game(self):
        sys.exit(0)


    def update(self):
        for button in self._buttons:
            button.update()


    def draw(self, screen: Surface):
        screen.blit(self._bg_image, (0, 0))

        for button in self._buttons:
            button.draw(screen)
