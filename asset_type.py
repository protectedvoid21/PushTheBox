from enum import Enum


class AssetType(Enum):
    MENU_BACKGROUND = 'background_menu'
    WALL = 'wall'
    WALL_SIDE = 'wall_side'
    BOX = 'box'
    TARGET = 'target'
    PLAYER = 'player'
    PLAYER_ANIMATIONS = 'animations'
    PLAY_BUTTON = 'play_button'
    EXIT_BUTTON = 'exit_button'
    BACK_BUTTON = 'back_button'
    RESTART_BUTTON = 'restart_button'
    RESUME_BUTTON = 'resume_button'
    MAIN_TITLE = 'main_title'