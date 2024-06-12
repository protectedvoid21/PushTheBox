from enum import Enum


class AssetType(Enum):
    """Enum representing the types of assets used in the game."""
    MENU_BACKGROUND = 'background_menu'
    WALL = 'wall'
    WALL_SIDE = 'wall_side'
    BOX = 'box'
    TARGET = 'target'
    PLAYER = 'player'
    PLAYER_ANIMATIONS = 'animations'

    GREEN_BUTTON = 'green_button'
    BLUE_BUTTON = 'blue_button'
    RED_BUTTON = 'red_button'

    MAIN_TITLE = 'main_title'
    BG_IMAGE = 'bg_image'
