from abc import ABC, abstractmethod
from dataclasses import dataclass

from pygame import Surface

from asset_manager import AssetManager


@dataclass
class State(ABC):
    """
        Abstract base class for a game state.

        A game state represents a specific condition or mode of the game, such as the main menu, gameplay, or game over screen.

        Attributes:
            _game_manager (any): The game manager object that controls the game loop and state transitions.
            asset_manager (AssetManager): The asset manager object that handles loading and storing of game assets.
    """
    _game_manager: any
    asset_manager: AssetManager


    def __init__(self):
        """
            Initialize the State.

            The game manager and asset manager are not set in the constructor because they are not known at the time of State creation.
            They are set later using the prepare method.
        """
        self._game_manager = None


    def prepare(self, game_manager, asset_manager):
        """
            Method injecting the game manager and asset manager into the State.
            
            This method is called before the State is transitioned into.
            Do not override this method without calling super().prepare(game_manager, asset_manager) first.
            
            Args:
                game_manager (any): The game manager object.
                asset_manager (AssetManager): The asset manager object.
        """
        self._game_manager = game_manager
        self.asset_manager = asset_manager


    @abstractmethod
    def update(self):
        """
            Update the State.

            This method is called once per frame and should contain code to update the state of the game objects, handle user input, etc.
        """
        ...


    @abstractmethod
    def draw(self, screen: Surface):
        """
            Draw all entities specified by state.
    
            This method is called once per frame after the update method 
            and should contain code to draw the state of the game objects to the screen.
    
            Args:
                screen (Surface): The Pygame surface to draw to.
        """
        ...
