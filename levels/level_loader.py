import os
from dataclasses import dataclass

import pygame.image
from pygame import Vector2

from asset_manager import AssetManager
from block import Block, BlockType
from constants import LEVELS_DIR, BLOCK_SIZE
from player import Player


@dataclass
class BlockData:
    block_type: BlockType
    pushable: bool = False
    solid: bool = False
    is_destination: bool = False


class LevelData:
    def __init__(self, blocks: list[Block], boxes: list[Block], destinations: list[Block], player: Player):
        self.blocks = blocks
        self.player = player
        self.boxes = boxes
        self.destinations = destinations


class LevelLoader:
    _asset_manager: AssetManager
    _blocks_dict: dict[str, BlockData] = {
        'X': BlockData(BlockType.DESTINATION, is_destination=True),
        'B': BlockData(BlockType.BOX, pushable=True),
        '@': BlockData(BlockType.WALL, solid=True),
    }

    def load(self, level_index: int) -> LevelData:
        level_path = os.path.join(LEVELS_DIR, f'{level_index}.txt')

        with open(level_path, 'r') as file:
            lines = file.readlines()

        blocks: list[Block] = []
        player: Player | None = None

        self._asset_manager = AssetManager()

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char in self._blocks_dict:
                    block_data = self._blocks_dict[char]

                    block_image = self._asset_manager.block_images[block_data.block_type]
                    block = Block(block_image,
                                  pygame.Rect(Vector2(j, i) * BLOCK_SIZE, (BLOCK_SIZE, BLOCK_SIZE)),
                                  block_data.pushable,
                                  block_data.solid,
                                  block_data.is_destination)

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
