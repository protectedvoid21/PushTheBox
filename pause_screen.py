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
    
    def __init__(self, resume_game_callback: callable, restart_callback: callable, back_to_menu_callback: callable, asset_manager: AssetManager):
        button_positions = ui_positioner.generate_positions_column(
            x_position=0, y_position=300, button_width=200, button_height=50, button_gap=50, button_count=3
        )

        self._buttons = [
            Button(button_positions[0], image=asset_manager[AssetType.RESUME_BUTTON], click_event=resume_game_callback),
            Button(button_positions[1], image=asset_manager[AssetType.RESTART_BUTTON], click_event=restart_callback),
            Button(button_positions[2], image=asset_manager[AssetType.EXIT_BUTTON], click_event=back_to_menu_callback)
        ]
        
        ui_positioner.center_buttons(self._buttons, pygame.display.get_window_size())

        self._game_title_img = asset_manager[AssetType.MAIN_TITLE]
        
        self._game_title_rect = Rect(0, 100, 400, 200)
        self._game_title_rect.centerx = pygame.display.get_window_size()[0] // 2
        print(self._game_title_rect.centerx)
        
    def update(self):
        for button in self._buttons:
            button.update()
            
            
    def draw(self, screen: Surface):
        background = Surface((screen.get_width(), screen.get_height()))
        background.fill(self._background_color)
        background.set_alpha(128)
        
        screen.blit(self._game_title_img, self._game_title_rect)
        
        screen.blit(background, (0, 0))
        
        for button in self._buttons:
            button.draw(screen)