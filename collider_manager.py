import math

from pygame import Vector2, Rect
from block import Block

MOVE_PREDICTION_THRESHOLD = 0.1

def get_push_direction(entity_rect: Rect, pushed_rect: Rect):
    vecs_subtracted = Vector2(pushed_rect.center) - Vector2(entity_rect.center)

    push_vector = Vector2(vecs_subtracted)
    
    if abs(push_vector.x) > abs(push_vector.y):
        return Vector2(math.copysign(1, push_vector.x), 0)
    else:
        return Vector2(0, math.copysign(1, push_vector.y))


def is_close_to(a: Vector2, b: Vector2, tolerance: float):
    return (a - b).magnitude() < tolerance


def can_move(blocks: list[Block], entity_rect: Rect, direction: Vector2):
    future_move = entity_rect.copy().move(direction)

    for block in blocks:
        if future_move.colliderect(block.rect):
            if block.is_solid:
                return False
            if block.is_pushable:
                if block.rect == entity_rect:
                    continue
                if can_move(blocks, block.rect, direction + MOVE_PREDICTION_THRESHOLD * direction):
                    dir_vector = get_push_direction(entity_rect, block.rect)
                    block.rect.move_ip(dir_vector * direction.magnitude())
                    return True
                return False

    return True