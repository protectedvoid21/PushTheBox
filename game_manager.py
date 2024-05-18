import sys
from dataclasses import dataclass

import pygame
from pygame import Surface

from constants import *
from game_time import GameTime
from in_game_state import InGameState
from levels.level_loader import LevelLoader
from state import State
from title_generator import generate_title


@dataclass
class GameManager:
    _screen: Surface
    _screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    _current_state: State = None
    _game_time = GameTime(FRAMERATE)
    
    def __init__(self):
        pygame.init()
        
        self._screen = pygame.display.set_mode(self._screen_size)
        pygame.display.set_caption(MAIN_TITLE + ' - ' + generate_title())
        
        #TEMP
        level_loader = LevelLoader()
        blocks, player = level_loader.load(1)
        #TEMP
        
        self._current_state = InGameState(blocks, player)
        self._current_state.prepare(self)
        
        
    def run(self):
        while self._current_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self._game_time.update()
            
            self._current_state.update()
            self._current_state.draw(self._screen)
            
            pygame.display.update()
        pygame.quit()