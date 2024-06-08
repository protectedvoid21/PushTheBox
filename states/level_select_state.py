from pygame import Surface

import ui_positioner
from asset_manager import AssetType
from button import Button
from level_loader import LevelLoader, LevelData
from states.in_game_state import InGameState
from states.state import State


class LevelSelectState(State):
    _level_loader: LevelLoader = LevelLoader()
    
    _buttons: list[Button] = []
    
    def __init__(self):
        super().__init__()

        positions = ui_positioner.generate_positions_column(
            x_position=200, y_position=100, button_gap=50, button_count=5, button_width=250, button_height=75
        )

        self._buttons = [
            Button(positions[i], text=f'Level {i + 1}', click_event=lambda x=i: self.select_level(x + 1))
            for i in range(5)
        ]
    
    def select_level(self, level_name: int):
        level_data: LevelData = self._level_loader.load(level_name)
        
        self._game_manager.change_state(InGameState(level_data, level_name))
    
    def update(self):
        for button in self._buttons:
            button.update()

    def draw(self, screen: Surface):
        screen.blit(self._asset_manager.asset_dict[AssetType.MENU_BACKGROUND], (0, 0))
        
        for button in self._buttons:
            button.draw(screen)