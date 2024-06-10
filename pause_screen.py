from collections.abc import Callable

import pygame
from pygame import Rect, Surface

import ui_positioner
from asset_manager import AssetManager
from asset_type import AssetType
from button import Button


class PauseScreen:
    _game_title_img: pygame.image
    _game_title_rect: Rect
    _background_color: tuple[int, int, int] = (0, 0, 0)
    _buttons: list[Button] = []


    def __init__(self, resume_game_callback: Callable, restart_callback: Callable, back_to_menu_callback: Callable, asset_manager: AssetManager):
        button_positions = ui_positioner.generate_positions_column(
            x_position=0, y_position=300, button_width=275, button_height=80, button_gap=75, button_count=3
        )

        self._buttons = [
            Button(button_positions[0], font=asset_manager.default_font, text='Resume', image=asset_manager[AssetType.GREEN_BUTTON], click_event=resume_game_callback),
            Button(button_positions[1], font=asset_manager.default_font, text='Restart', image=asset_manager[AssetType.BLUE_BUTTON], click_event=restart_callback),
            Button(button_positions[2], font=asset_manager.default_font, text='Exit', image=asset_manager[AssetType.RED_BUTTON], click_event=back_to_menu_callback)
        ]

        ui_positioner.center_objects_x(list(map(lambda x: x.rect, self._buttons)), pygame.display.get_window_size())

        self._game_title_img = asset_manager[AssetType.MAIN_TITLE]

        self._game_title_rect = Rect(0, 100, 700, 200)
        self._game_title_rect.centerx = pygame.display.get_window_size()[0] // 2


    def update(self):
        for button in self._buttons:
            button.update()


    def draw(self, screen: Surface):
        background = Surface((screen.get_width(), screen.get_height()))
        background.fill(self._background_color)
        background.set_alpha(128)


        screen.blit(background, (0, 0))
        
        screen.blit(self._game_title_img, self._game_title_rect)

        for button in self._buttons:
            button.draw(screen)
