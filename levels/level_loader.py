import os
from dataclasses import dataclass

import pygame.image
from pygame import Vector2

from block import Block
from constants import LEVELS_DIR, BLOCK_SIZE
from player import Player


@dataclass
class BlockData:
    image_path: str
    pushable: bool = False
    solid: bool = False


class LevelLoader:
    _blocks_dict: dict[str, BlockData] = {
        'X': BlockData('assets/dest.png'),
        'B': BlockData('assets/box.png', pushable=True),
        '@': BlockData('assets/wall.png', solid=True),
    }

    def load(self, level_index: int) -> tuple[list[Block], Player]:
        level_path = os.path.join(LEVELS_DIR, f'{level_index}.txt')

        with open(level_path, 'r') as file:
            lines = file.readlines()

        blocks: list[Block] = []
        player: Player | None = None

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char in self._blocks_dict:
                    block_data = self._blocks_dict[char]

                    block_image = pygame.image.load(self._blocks_dict[char].image_path)
                    block_image = pygame.transform.scale(block_image, (BLOCK_SIZE, BLOCK_SIZE))
                    block = Block(block_image,
                                  pygame.Rect(Vector2(j, i) * BLOCK_SIZE, (BLOCK_SIZE, BLOCK_SIZE)),
                                  block_data.pushable,
                                  block_data.solid)

                    blocks.append(block)

                if char == 'P':
                    player_image = pygame.image.load('assets/player.png')
                    player_image = pygame.transform.scale(player_image, (BLOCK_SIZE, BLOCK_SIZE))
                    player = Player(player_image, Vector2(j, i) * BLOCK_SIZE)

        if player is None:
            raise ValueError('Player not found in level')

        return blocks, player
