from player import Player
from state import State


class InGameState(State):
    _player: Player

    def __init__(self, screen, state_manager):
        super().__init__(screen, state_manager)
        
    def update(self):
        pass

    def draw(self):
        self._screen.fill((0, 0, 0))