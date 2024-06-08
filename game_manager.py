import sys
from dataclasses import dataclass

import pygame
from pygame import Surface

from asset_manager import AssetManager
from constants import *
from event_manager import EventManager
from game_time import GameTime
from states.menu_state import MenuState
from states.state import State
from title_generator import generate_title


@dataclass
class GameManager:
    _screen: Surface
    _asset_manager: AssetManager
    _screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    _current_state: State = None
    _game_time = GameTime(FRAMERATE)
    
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        self._screen = pygame.display.set_mode(self._screen_size)
        pygame.display.set_caption(MAIN_TITLE + ' - ' + generate_title())
        
        self._asset_manager = AssetManager()
        
        # self.change_state(InGameState(LevelLoader().load(1), 1))
        self.change_state(MenuState())
        
    def change_state(self, state: State):
        self._current_state = state
        self._current_state.prepare(self, self._asset_manager)
        
        
    def run(self):
        while self._current_state:
            self._game_time.update()
            EventManager.update()
            
            events = EventManager.get_events()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            
            self._current_state.update()
            self._current_state.draw(self._screen)
            
            pygame.display.update()
        pygame.quit()