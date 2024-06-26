import os
from dataclasses import dataclass

import pygame
import yaml

from asset_type import AssetType
from constants import BLOCK_SIZE, PLAYER_TILE_SIZE, PLAYER_SIZE, TEXTURES_PATH_DIR
from player import Direction

ASSETS_FOLDER_PATH = 'assets'


@dataclass
class AssetManager:
    """
        Manages the assets of the game. Serves as a central repository for all game assets.
        
        Assets can be accessed by their type, e.g. AssetManager[AssetType.PLAYER].
    """
    _player_image: pygame.image
    _player_animations: dict[Direction, list[pygame.image]]
    default_font: pygame.font.Font

    _texture_paths: any

    _asset_dict: dict[AssetType, pygame.image]


    def __init__(self):
        """
            Initialize the AssetManager.

            Loads the assets and initializes the player image, player animations, and default font.
        """
        self._asset_dict = self._load_assets()

        pygame.font.init()
        self.default_font = pygame.font.Font(os.path.join(ASSETS_FOLDER_PATH, 'osd_mono.ttf'), 56)

        for block_type in [AssetType.WALL, AssetType.WALL_SIDE, AssetType.BOX, AssetType.TARGET]:
            self._asset_dict[block_type] = pygame.transform.scale(self._asset_dict[block_type],
                                                                  (BLOCK_SIZE, BLOCK_SIZE))

        self._asset_dict[AssetType.BG_IMAGE] = pygame.transform.scale(self[AssetType.BG_IMAGE], (BLOCK_SIZE, BLOCK_SIZE))
        self._player_image = pygame.transform.scale(self._asset_dict[AssetType.PLAYER], PLAYER_SIZE)
        self._player_animations = self._parse_animations()


    def _load_assets(self) -> dict[AssetType, pygame.image]:
        with open(TEXTURES_PATH_DIR, 'r') as file:
            self._texture_paths = yaml.load(file, Loader=yaml.FullLoader)['textures']

        asset_dict = {}

        for asset_type in AssetType:
            asset_name = self._texture_paths[asset_type.value]
            asset_image = pygame.image.load(os.path.join(ASSETS_FOLDER_PATH, asset_name))
            asset_dict[asset_type] = asset_image

        return asset_dict


    def _parse_animations(self) -> dict[Direction, list[pygame.image]]:
        """
            Parse the player animations from the player animations image.
    
            Returns:
                dict[Direction, list[pygame.image]]: A dictionary mapping directions to lists of images.
        """
        animation_image = self._asset_dict[AssetType.PLAYER_ANIMATIONS].convert_alpha()
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


    def __getitem__(self, item: AssetType) -> pygame.image:
        """
            Get the image of the given asset type.
    
            Args:
                item (AssetType): The asset type.
    
            Returns:
                pygame.image: The image of the asset type.
        """
        return self._asset_dict[item]


    @property
    def player_image(self) -> pygame.image:
        return self._player_image


    @property
    def player_animations(self) -> dict[Direction, list[pygame.image]]:
        return self._player_animations


    @property
    def asset_dict(self) -> dict[AssetType, pygame.image]:
        return self._asset_dict
