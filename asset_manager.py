import os
from dataclasses import dataclass

import pygame
import yaml

from block import BlockType
from constants import BLOCK_SIZE, PLAYER_TILE_SIZE, PLAYER_SIZE, TEXTURES_PATH_DIR
from player import Direction

ASSETS_FOLDER_PATH = 'assets'

@dataclass
class AssetManager:
    _player_image: pygame.image
    _player_animations: dict[Direction, list[pygame.image]]
    _block_images: dict[BlockType, pygame.image]
    
    _texture_paths: any
    
    def __init__(self):
        with open(TEXTURES_PATH_DIR, 'r') as file:
            self._texture_paths = yaml.load(file, Loader=yaml.FullLoader)['textures']
        
        self._player_image = pygame.image.load(os.path.join(ASSETS_FOLDER_PATH, self._texture_paths['player']['image']))
        self._player_image = pygame.transform.scale(self._player_image, PLAYER_SIZE)
        
        block_lookup = {
            BlockType.WALL: 'wall',
            BlockType.WALL_SIDE: 'wall_side',
            BlockType.BOX: 'box',
            BlockType.TARGET: 'target',
        }
        
        self._block_images = {}
        
        for block_type, path in block_lookup.items():
            self._block_images[block_type] = pygame.image.load(os.path.join(ASSETS_FOLDER_PATH, self._texture_paths['blocks'][path]))
            self._block_images[block_type] = pygame.transform.scale(self._block_images[block_type], (BLOCK_SIZE, BLOCK_SIZE))
                    
        self._player_animations = self._parse_animations()
        
                        
    def _parse_animations(self) -> dict[Direction, list[pygame.image]]:
        player_animations_path = os.path.join(ASSETS_FOLDER_PATH, 'player_animations.png')

        animation_image = pygame.image.load(player_animations_path).convert_alpha()
        directions = [Direction.DOWN, Direction.LEFT, Direction.RIGHT, Direction.UP]
        
        animation_dict = {}
        
        for i, direction in enumerate(directions):
            animation_dict[direction] = []
            
            for j in range(3):
                x = j * PLAYER_TILE_SIZE[0]
                y = i * PLAYER_TILE_SIZE[1]
                
                image = animation_image.subsurface(pygame.Rect(x, y, PLAYER_TILE_SIZE[0], PLAYER_TILE_SIZE[1]))
                image = pygame.transform.scale(image, PLAYER_SIZE)
                animation_dict[direction].append(image)
                
        return animation_dict
        
        
    @property
    def player_image(self) -> pygame.image:
        return self._player_image
    
    @property
    def player_animations(self) -> dict[Direction, list[pygame.image]]:
        return self._player_animations
    
    @property
    def block_images(self) -> dict[BlockType, pygame.image]:
        return self._block_images
        