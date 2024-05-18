from dataclasses import dataclass

from pygame import Surface

from block import Block
from entity_manager import EntityManager
from player import Player
from state import State


@dataclass
class InGameState(State):
    _player: Player
    _blocks: list[Block]
    _entity_manager: EntityManager

    def __init__(self, blocks: list[Block], player: Player):
        self._blocks = blocks
        self._player = player
        self._entity_manager = EntityManager(blocks, player)

    def prepare(self, game_manager):
        super().prepare(game_manager)
                
                
    def update(self):
        player_direction = self._player.get_move_direction()
        
        if self._entity_manager.can_move(player_direction):
            self._player.move(player_direction)


    def draw(self, screen: Surface):
        screen.fill((0, 0, 0))
        self._player.draw(screen)
        
        for block in self._blocks:
            screen.blit(block.image, block.rect)