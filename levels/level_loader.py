import os

import pygame.image

from block import Block
from constants import LEVELS_DIR
from vector import Vector


class LevelLoader:
    _blocks_dict = {
        'X': 'assets/dest.png',
        'P': 'assets/player.png',
        'B': 'assets/box.png',
        '@': 'assets/wall.png'
    }
    
    def load(self, level_index: int) -> list[Block]:
        level_path = os.path.join(LEVELS_DIR, f'{level_index}.txt')
        
        with open(level_path, 'r') as file:
            lines = file.readlines()
        
        blocks: list[Block] = []
        
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char in self._blocks_dict:
                    block_image = pygame.image.load(self._blocks_dict[char])
                    block = Block(block_image, Vector(j * 50, i * 50))
                    
                    blocks.append(block)
                    
        
        return blocks