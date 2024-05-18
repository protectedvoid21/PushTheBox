import os

import pygame.image
from pygame import Vector2

from block import Block
from constants import LEVELS_DIR, BLOCK_SIZE
from player import Player


class LevelLoader:
    _blocks_dict = {
        'X': 'assets/dest.png',
        'B': 'assets/box.png',
        '@': 'assets/wall.png'
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
                    block_image = pygame.image.load(self._blocks_dict[char])
                    block_image = pygame.transform.scale(block_image, (BLOCK_SIZE, BLOCK_SIZE))
                    block = Block(block_image, Vector2(j, i) * BLOCK_SIZE)
                    
                    blocks.append(block)
                    
                if char == 'P':
                    player_image = pygame.image.load('assets/player.png')
                    player_image = pygame.transform.scale(player_image, (BLOCK_SIZE, BLOCK_SIZE))
                    player = Player(player_image, Vector2(j, i) * BLOCK_SIZE)
                
        if player is None:
            raise ValueError('Player not found in level')
        
        return blocks, player