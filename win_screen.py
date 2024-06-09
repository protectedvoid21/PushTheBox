from collections.abc import Callable
from dataclasses import dataclass

import pygame
from pygame import Surface

import ui_positioner
from asset_manager import AssetManager
from asset_type import AssetType
from button import Button


@dataclass
class WinScreen:
    _buttons: list[Button]
    _bg_color: tuple[int, int, int] = (0, 0, 0)


    def __init__(self,
                 asset_manager: AssetManager,
                 next_level_callback: Callable,
                 restart_callback: Callable,
                 back_to_menu_callback: Callable):
        positions = ui_positioner.generate_positions_column(
            x_position=0, y_position=500, button_width=275, button_height=80, button_gap=50, button_count=3
        )

        self._buttons = [
            Button(positions[0], font=asset_manager.default_font, text='Next lvl', image=asset_manager[AssetType.GREEN_BUTTON], click_event=next_level_callback),
            Button(positions[1], font=asset_manager.default_font, text='Restart',image=asset_manager[AssetType.BLUE_BUTTON], click_event=restart_callback),
            Button(positions[2], font=asset_manager.default_font, text='Exit', image=asset_manager[AssetType.RED_BUTTON], click_event=back_to_menu_callback)
        ]

        ui_positioner.center_buttons_x(self._buttons, pygame.display.get_window_size())


    def update(self):
        for button in self._buttons:
            button.update()


    def draw(self, screen: Surface):
        background = Surface((screen.get_width(), screen.get_height()))
        background.fill(self._bg_color)
        background.set_alpha(128)

        screen.blit(background, (0, 0))

        for button in self._buttons:
            button.draw(screen)
