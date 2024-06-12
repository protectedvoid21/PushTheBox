from dataclasses import dataclass

import pygame.event
from pygame import Surface, Vector2

import constants
import event_manager
from block import Block
from camera import Camera
from collider_manager import can_move, is_close_to
from constants import BOX_DISTANCE_TOLERANCE_PERCENTAGE
from level_loader import LevelData
from pause_screen import PauseScreen
from player import Player
from states.state import State
from win_screen import WinScreen


@dataclass
class InGameState(State):
    _player: Player
    _camera: Camera
    _blocks: list[Block]
    
    _boxes: list[Block]
    _destinations: list[Block]
    _level_data: LevelData

    _level_number: int

    _pause_screen: PauseScreen
    _win_screen: WinScreen
    _is_won: bool = False
    _is_paused: bool = False


    def __init__(self, level_data: LevelData, level_number: int):
        """
            Initialize the InGameState with the given level data and level number.

            Args:
                level_data (LevelData): The data of the level to be played.
                level_number (int): The number of the level to be played.
        """
        super().__init__()
        self._level_number = level_number

        self._player = level_data.player
        self._blocks = level_data.blocks
        self._boxes = level_data.boxes
        self._destinations = level_data.destinations

        self._camera = Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)


    def prepare(self, game_manager, asset_manager):
        super().prepare(game_manager, asset_manager)
        self._pause_screen = PauseScreen(self.resume_game, self.restart_game, self.back_to_menu, asset_manager)
        self._win_screen = WinScreen(asset_manager, lambda: self.next_level(), self.restart_game, self.back_to_menu, self._level_number)
        

    def update(self):
        for event in event_manager.EventManager.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._is_paused = not self._is_paused


        self._is_won = self.check_if_won()
        if self._is_won:
            self._win_screen.update()
            return

        if self._is_paused:
            self._pause_screen.update()
            return

        player_direction = self._player.get_move_direction()

        if can_move(self._blocks, self._player.rect, player_direction):
            self._player.move(player_direction)
            self._camera.update(self._player.rect)


    def check_if_won(self) -> bool:
        """
            Check if the game has been won.

            Returns:
                bool: True if the game has been won, False otherwise.
        """
        for box in self._boxes:
            distance_tolerance = box.rect.width / BOX_DISTANCE_TOLERANCE_PERCENTAGE

            if not any(is_close_to(Vector2(box.rect.center), Vector2(dest.rect.center), distance_tolerance)
                       for dest in self._destinations):
                return False

        return True


    def resume_game(self):
        """Resume the game if it is paused."""
        self._is_paused = False


    def restart_game(self):
        """Restart the game."""
        from states.level_select_state import LevelSelectState
        select_level_state = LevelSelectState()

        self._game_manager.change_state(select_level_state)
        select_level_state.select_level(self._level_number)


    def next_level(self):
        """Proceeds to next level with number equal to the current level number plus one."""
        from states.level_select_state import LevelSelectState
        select_level_state = LevelSelectState()

        self._game_manager.change_state(select_level_state)
        select_level_state.select_level(self._level_number + 1)


    def back_to_menu(self):
        """Go back to the main menu."""
        from states.menu_state import MenuState
        self._game_manager.change_state(MenuState())


    def draw(self, screen: Surface):
        screen.fill((25,25,25))
        
        for block in self._blocks:
            screen.blit(block.image, self._camera.apply(block.rect))

        self._player.draw(screen, self._camera)

        if self._is_won:
            self._win_screen.draw(screen)
            return

        if self._is_paused:
            self._pause_screen.draw(screen)
