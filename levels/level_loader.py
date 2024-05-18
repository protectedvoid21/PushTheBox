import os

import pygame.image
from pygame import Vector2

from block import Block
from constants import LEVELS_DIR, BLOCK_SIZE

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
                    block_image = pygame.transform.scale(block_image, (BLOCK_SIZE, BLOCK_SIZE))
                    block = Block(block_image, Vector2(j * 50, i * 50))
                    
                    blocks.append(block)
                    
        
        return blocks