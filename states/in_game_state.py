from dataclasses import dataclass

from pygame import Surface, Vector2

from block import Block
from collider_manager import can_move, is_close_to
from constants import BOX_DISTANCE_TOLERANCE_PERCENTAGE
from level_loader import LevelData
from player import Player
from states.state import State


@dataclass
class InGameState(State):
    _player: Player
    _blocks: list[Block]

    _boxes: list[Block]
    _destinations: list[Block]

    def __init__(self, level_data: LevelData):
        super().__init__()
        self._player = level_data.player
        self._blocks = level_data.blocks
        self._boxes = level_data.boxes
        self._destinations = level_data.destinations


    def update(self):
        player_direction = self._player.get_move_direction()

        if can_move(self._blocks, self._player.rect, player_direction):
            self._player.move(player_direction)
            
        if self.is_won():
            print('You won!')


    def is_won(self) -> bool:
        for box in self._boxes:
            distance_tolerance = box.rect.width / BOX_DISTANCE_TOLERANCE_PERCENTAGE
            
            if not any(is_close_to(Vector2(box.rect.center), Vector2(dest.rect.center), distance_tolerance)
                       for dest in self._destinations):
                return False

        return True
    

    def draw(self, screen: Surface):
        screen.fill((0, 0, 0))
        self._player.draw(screen)

        for block in self._blocks:
            screen.blit(block.image, block.rect)
