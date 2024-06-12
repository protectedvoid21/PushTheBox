import os
from dataclasses import dataclass

import pygame.image
from pygame import Vector2, Surface

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
    z_index: int = 0


def neighbor_count(x: int, y: int, map: list[str]) -> int:
    """
        Calculate the number of neighbors for a given block in the map.
    
        Args:
            x (int): The x-coordinate of the block.
            y (int): The y-coordinate of the block.
            map (list[str]): The 2D map of the level.
    
        Returns:
            int: The number of neighbors of the block.
    """
    count = 0
    
    if x > 0 and map[y][x - 1] != ' ':
        count += 1
    if x < len(map[y]) - 1 and map[y][x + 1] != ' ':
        count += 1
    if y > 0 and map[y - 1][x] != ' ':
        count += 1
    if y < len(map) - 1 and map[y + 1][x] != ' ':
        count += 1
        
    return count


def is_block_bottom_corner(x: int, y: int, map: list[str]) -> bool:
    """
        Check if a block is a bottom corner block.
    
        A block is considered a bottom corner block if it has exactly two neighbors and it is not on the top row.
    
        Args:
            x (int): The x-coordinate of the block.
            y (int): The y-coordinate of the block.
            map (list[str]): The 2D map of the level.
    
        Returns:
            bool: True if the block is a bottom corner block, False otherwise.
    """
    block_char = map[y][x]
    
    neighbors = neighbor_count(x, y, map)
    
    if neighbors != 2 or y == 0:
        return False
    
    if y == len(map) - 1:
        return True
    
    return map[y - 1][x] == block_char and map[y + 1][x] != block_char


def is_block_side(x: int, y: int, map: list[str]) -> bool:
    """
        Check if a block is a side block.
    
        A block is considered a side block if it is not a bottom corner block and 
        it has a neighbor below it or it has exactly two neighbors.
    
        Args:
            x (int): The x-coordinate of the block.
            y (int): The y-coordinate of the block.
            map (list[str]): The 2D map of the level.
    
        Returns:
            bool: True if the block is a side block, False otherwise.
    """
    block_char = map[y][x]
    
    if is_block_bottom_corner(x, y, map):
        return False
    
    neighbors = neighbor_count(x, y, map)
    
    if y < len(map) - 1 and map[y + 1][x] == block_char:
        return True

    if y == len(map) - 1:
        return False
    
    return map[y - 1][x] == block_char and map[y + 1][x] == block_char or (map[y + 1][x] == block_char and neighbors == 2)


class LevelData:
    """Represents the data required to load for level in the game."""
    def __init__(self, blocks: list[Block], boxes: list[Block], destinations: list[Block], player: Player):
        """
            Initialize the LevelData with the given blocks, boxes, destinations, and player.
    
            Args:
                blocks (list[Block]): A list of all blocks in the level.
                boxes (list[Block]): A list of all boxes in the level.
                destinations (list[Block]): A list of all destination blocks in the level.
                player (Player): The player object.
        """
        self.blocks = blocks
        self.player = player
        self.boxes = boxes
        self.destinations = destinations


class LevelLoader:
    """Converts the level structures from a file into a playable level."""
    
    _asset_manager: AssetManager
    _level_structures: dict
    _blocks_dict: dict[str, BlockData] = {
        'X': BlockData(AssetType.TARGET, is_target=True, z_index=1),
        'B': BlockData(AssetType.BOX, pushable=True, z_index=2),
        'W': BlockData(AssetType.WALL, solid=True, z_index=10),
        ' ': BlockData(AssetType.BG_IMAGE, solid=False, pushable=False, is_target=False, z_index=-1)
    }


    def __init__(self):
        """Initialize the LevelLoader. Reads the level structures from the levels file."""
        with open(LEVELS_DIR, 'r') as file:
            lines = file.read()
            self._level_structures = yaml.load(lines, Loader=yaml.FullLoader)
            self._level_structures = self._level_structures['levels']
            
            
    def _map_blockdata_to_block(self, block_data: BlockData, position: Vector2, override_img: Surface = None) -> Block:
        """
            Map block data to a block.
    
            Args:
                block_data (BlockData): The block data to map.
                position (Vector2): The position of the block.
                override_img (Surface, optional): An image to override the block's default image. Defaults to None.
    
            Returns:
                Block: The resulting block.
        """
        block_image = override_img if override_img else self._asset_manager.asset_dict[block_data.block_type]
        
        return Block(block_image,
                     pygame.Rect(position * BLOCK_SIZE, (BLOCK_SIZE, BLOCK_SIZE)),
                     block_data.pushable,
                     block_data.solid,
                     block_data.is_target,
                     block_data.z_index)
            

    def load(self, level_number: int) -> LevelData:
        """
            Load a level.
    
            Args:
                level_number (int): The number of the level to load.
    
            Returns:
                LevelData: The data of the loaded level.
        """
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

                    block = self._map_blockdata_to_block(block_data, Vector2(j, i), override_img=block_image)

                    blocks.append(block)

                if char != '-':
                    bg_block = self._blocks_dict[' ']
                    bg = self._map_blockdata_to_block(bg_block, Vector2(j, i))
                    blocks.append(bg)

                if char == 'P':
                    player = Player(self._asset_manager.player_image,
                                    Vector2(j, i) * BLOCK_SIZE,
                                    self._asset_manager.player_animations)

        if player is None:
            raise ValueError('Player not found in level')
        
        blocks = sorted(blocks, key=lambda x: x.z_index)

        return LevelData(blocks,
                         boxes=[block for block in blocks if block.is_pushable],
                         destinations=[block for block in blocks if block.is_destination],
                         player=player)
