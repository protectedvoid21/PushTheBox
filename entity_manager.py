from dataclasses import dataclass

from pygame import Vector2

from block import Block
from player import Player


@dataclass
class EntityManager:
    _blocks: list[Block]
    _player: Player
    
    def __init__(self, blocks: list[Block], player: Player):
        self._blocks = blocks
        self._player = player
        
    def can_move(self, direction: Vector2):
        player_rect = self._player.rect
        
        future_move = player_rect.copy().move(direction)
        
        for block in self._blocks:
            if future_move.colliderect(block.rect):
                if block.is_solid:
                    return False
                if block.is_pushable:
                    block.rect.move_ip(direction)
                    
        return True