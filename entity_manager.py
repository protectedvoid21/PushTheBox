import math
from dataclasses import dataclass

from pygame import Vector2, Rect

from block import Block
from player import Player


@dataclass
class EntityManager:
    _blocks: list[Block]
    _player: Player

    def __init__(self, blocks: list[Block], player: Player):
        self._blocks = blocks
        self._player = player

    def can_move(self, entity_rect: Rect, direction: Vector2):
        future_move = entity_rect.copy().move(direction)

        for block in self._blocks:
            if future_move.colliderect(block.rect):
                if block.is_solid:
                    return False
                if block.is_pushable:
                    if block.rect == entity_rect:
                        continue
                    if self.can_move(block.rect, direction):
                        dir_vector = self.get_push_direction(entity_rect, block.rect)
                        block.rect.move_ip(dir_vector * direction.magnitude())
                        return True
                    return False

        return True
    

    def get_push_direction(self, entity_rect: Rect, pushed_rect: Rect):
        vecs_subtracted = Vector2(pushed_rect.center) - Vector2(entity_rect.center)
    
        push_vector = Vector2(vecs_subtracted)
        
        if abs(push_vector.x) > abs(push_vector.y):
            return Vector2(math.copysign(1, push_vector.magnitude()), 0)
        else:
            return Vector2(0, math.copysign(1, push_vector.magnitude()))