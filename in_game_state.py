import pygame

from player import Player
from state import State


class InGameState(State):
    _player: Player

    def __init__(self, screen, state_manager):
        super().__init__(screen, state_manager)
        self._player = Player(pygame.image.load('assets/player.png'), speed=100)
        
    def update(self):
        self._player.handle_input()

    def draw(self):
        self._screen.fill((0, 0, 0))
        self._player.draw(self._screen)