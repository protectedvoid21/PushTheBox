import pygame
from pygame import Rect, Surface

import ui_positioner
from button import Button


class PauseScreen:
    _background_color: tuple[int, int, int] = (0, 0, 0)
    _buttons: list[Button] = []
    
    def __init__(self, resume_game_callback: callable, restart_callback: callable, back_to_menu_callback: callable):
        button_positions = ui_positioner.generate_positions_column(500, 300, 200, 50, 50, 3)
        
        self._buttons = [
            Button(button_positions[0], 'Resume', resume_game_callback),
            Button(button_positions[1], 'Restart', restart_callback),
            Button(button_positions[2], 'Exit', back_to_menu_callback)
        ]
        
        
    def update(self):
        for button in self._buttons:
            button.update()
            
            
    def draw(self, screen: Surface):
        screen.fill(self._background_color)
        
        for button in self._buttons:
            button.draw(screen)