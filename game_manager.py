import sys
from dataclasses import dataclass

import pygame
from pygame import Surface

from constants import *
from game_time import GameTime
from in_game_state import InGameState
from state import State
from title_generator import generate_title


@dataclass
class GameManager:
    _surface: Surface
    _screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    _current_state: State = None
    _game_time = GameTime(FRAMERATE)
    
    def __init__(self):
        pygame.init()
        
        self._surface = pygame.display.set_mode(self._screen_size)
        pygame.display.set_caption(MAIN_TITLE + ' - ' + generate_title())
        self._current_state = InGameState(self._surface, self)
        
        
    def run(self):
        while self._current_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self._game_time.update()
            
            self._current_state.update()
            self._current_state.draw()
            
            pygame.display.update()
        pygame.quit()