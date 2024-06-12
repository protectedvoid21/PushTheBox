from collections.abc import Callable
from dataclasses import dataclass

import pygame
from pygame import Surface, Rect

import asset_manager
import ui_positioner
from asset_manager import AssetManager
from asset_type import AssetType
from button import Button


@dataclass
class WinScreen:
    """Represents the win screen in the game."""
    _buttons: list[Button]
    _desc_rect: Rect
    _sub_desc_rect: Rect
    _asset_manager: AssetManager
    _desc_text: str = 'You won!'
    _sub_desc_text: str = 'You have completed level'
    _bg_color: tuple[int, int, int] = (0, 0, 0)


    def __init__(self,
                 asset_manager: AssetManager,
                 next_level_callback: Callable,
                 restart_callback: Callable,
                 back_to_menu_callback: Callable,
                 level_number: int):
        """
        Initialize the WinScreen with the given asset manager, callbacks, and level number.

        Args:
            asset_manager (AssetManager): The asset manager.
            next_level_callback (Callable): The callback function to go to the next level.
            restart_callback (Callable): The callback function to restart the level.
            back_to_menu_callback (Callable): The callback function to go back to the menu.
            level_number (int): The number of the level that was completed.
        """
        self._sub_desc_text = f'{self._sub_desc_text} {level_number}!'
        self._asset_manager = asset_manager
        
        positions = ui_positioner.generate_positions_column(
            x_position=0, y_position=500, button_width=275, button_height=80, button_gap=50, button_count=3
        )

        self._buttons = [
            Button(positions[0], font=asset_manager.default_font, text='Next lvl', image=asset_manager[AssetType.GREEN_BUTTON], click_event=next_level_callback),
            Button(positions[1], font=asset_manager.default_font, text='Restart',image=asset_manager[AssetType.BLUE_BUTTON], click_event=restart_callback),
            Button(positions[2], font=asset_manager.default_font, text='Exit', image=asset_manager[AssetType.RED_BUTTON], click_event=back_to_menu_callback)
        ]

        ui_positioner.center_objects_x(list(map(lambda x: x.rect, self._buttons)), pygame.display.get_window_size())
        
        self._desc_rect = Rect(0, 100, 700, 200)
        self._sub_desc_rect = Rect(0, 200, 700, 200)
        
        ui_positioner.center_objects_x([self._desc_rect, self._sub_desc_rect], pygame.display.get_window_size())


    def update(self):
        """
        Update the win screen.

        This method should be called once per frame. It updates the buttons on the win screen.
        """
        for button in self._buttons:
            button.update()


    def draw(self, screen: Surface):
        """
        Draw the win screen.

        Args:
            screen (Surface): The game screen.
        """
        background = Surface((screen.get_width(), screen.get_height()))
        background.fill(self._bg_color)
        background.set_alpha(128)

        screen.blit(background, (0, 0))

        text = self._asset_manager.default_font.render(self._desc_text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self._desc_rect.center)
        
        sub_text = self._asset_manager.default_font.render(self._sub_desc_text, True, (255, 255, 255))
        sub_text_rect = sub_text.get_rect(center=self._sub_desc_rect.center)
        
        screen.blit(text, text_rect)
        screen.blit(sub_text, sub_text_rect)

        for button in self._buttons:
            button.draw(screen)
