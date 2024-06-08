import os
from dataclasses import dataclass

import pygame.image
from pygame import Vector2

from asset_manager import AssetManager, AssetType
from block import Block
from constants import LEVELS_DIR, BLOCK_SIZE
from player import Player

import yaml


@dataclass
class BlockData:
    block_type: AssetType
    pushable: bool = False
    solid: bool = False
    is_target: bool = False


def is_block_side(x: int, y: int, map: list[str]) -> bool:
    block_char = map[y][x]

    if y > 0 and map[y - 1][x] == block_char:
        return True
    if y < len(map) - 1 and map[y + 1][x] == block_char:
        return True
    return False


class LevelData:
    def __init__(self, blocks: list[Block], boxes: list[Block], destinations: list[Block], player: Player):
        self.blocks = blocks
        self.player = player
        self.boxes = boxes
        self.destinations = destinations


class LevelLoader:
    _asset_manager: AssetManager
    _level_structures: dict
    _blocks_dict: dict[str, BlockData] = {
        'X': BlockData(AssetType.TARGET, is_target=True),
        'B': BlockData(AssetType.BOX, pushable=True),
        'W': BlockData(AssetType.WALL, solid=True),
    }

    def __init__(self):
        with open(LEVELS_DIR, 'r') as file:
            lines = file.read()
            self._level_structures = yaml.load(lines, Loader=yaml.FullLoader)
            self._level_structures = self._level_structures['levels']

    def load(self, level_number: int) -> LevelData:
        lines = self._level_structures[level_number]

        blocks: list[Block] = []
        player: Player | None = None

        self._asset_manager = AssetManager()

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char in self._blocks_dict:
                    block_data = self._blocks_dict[char]

                    block_image = self._asset_manager.asset_dict[block_data.block_type]

                    if block_data.block_type == AssetType.WALL and is_block_side(j, i, lines):
                        block_image = self._asset_manager.asset_dict[AssetType.WALL_SIDE]

                    block = Block(block_image,
                                  pygame.Rect(Vector2(j, i) * BLOCK_SIZE, (BLOCK_SIZE, BLOCK_SIZE)),
                                  block_data.pushable,
                                  block_data.solid,
                                  block_data.is_target)

                    blocks.append(block)

                if char == 'P':
                    player = Player(self._asset_manager.player_image,
                                    Vector2(j, i) * BLOCK_SIZE,
                                    self._asset_manager.player_animations)

        if player is None:
            raise ValueError('Player not found in level')

        return LevelData(blocks,
                         boxes=[block for block in blocks if block.is_pushable],
                         destinations=[block for block in blocks if block.is_destination],
                         player=player)
