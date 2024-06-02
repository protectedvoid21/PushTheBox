from dataclasses import dataclass

import pygame.event
from pygame import Surface, Vector2

import event_manager
from block import Block
from collider_manager import can_move, is_close_to
from constants import BOX_DISTANCE_TOLERANCE_PERCENTAGE, BACKGROUND_COLOR
from level_loader import LevelData
from pause_screen import PauseScreen
from player import Player
from states.state import State


@dataclass
class InGameState(State):
    _player: Player
    _blocks: list[Block]

    _boxes: list[Block]
    _destinations: list[Block]
    _level_data: LevelData
    
    _level_number: int

    _pause_screen: PauseScreen
    _is_won: bool = False
    _is_paused: bool = False


    def __init__(self, level_data: LevelData, level_number: int):
        super().__init__()
        self._level_number = level_number
        self._pause_screen = PauseScreen(self.resume_game, self.restart_game, self.back_to_menu)

        self._player = level_data.player
        self._blocks = level_data.blocks
        self._boxes = level_data.boxes
        self._destinations = level_data.destinations

    def update(self):
        if event_manager.EventManager.get_events():
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self._is_paused = not self._is_paused

        if self._is_paused:
            self._pause_screen.update()
            return

        player_direction = self._player.get_move_direction()

        if can_move(self._blocks, self._player.rect, player_direction):
            self._player.move(player_direction)

        if not self._is_won:
            self._is_won = self.check_if_won()

    def check_if_won(self) -> bool:
        for box in self._boxes:
            distance_tolerance = box.rect.width / BOX_DISTANCE_TOLERANCE_PERCENTAGE

            if not any(is_close_to(Vector2(box.rect.center), Vector2(dest.rect.center), distance_tolerance)
                       for dest in self._destinations):
                return False

        return True
    
    
    def resume_game(self):
        self._is_paused = False
    
    
    def restart_game(self):
        from states.level_select_state import LevelSelectState
        select_level_state = LevelSelectState()
        
        self._game_manager.change_state(select_level_state)
        
        select_level_state.select_level(self._level_number)
        
    def back_to_menu(self):
        from states.menu_state import MenuState
        self._game_manager.change_state(MenuState())
    

    def draw(self, screen: Surface):
        screen.fill(BACKGROUND_COLOR)
        self._player.draw(screen)

        for block in self._blocks:
            screen.blit(block.image, block.rect)

        if self._is_paused:
            self._pause_screen.draw(screen)