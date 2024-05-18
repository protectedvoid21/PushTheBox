from dataclasses import dataclass

import pygame
from pygame import Surface

from block import Block
from player import Player
from state import State


@dataclass
class InGameState(State):
    _player: Player
    _blocks: list[Block]

    def __init__(self, blocks: list[Block]):
        self._blocks = blocks
        self._player = Player(pygame.image.load('assets/player.png'), speed=100)

    def prepare(self, game_manager):
        super().prepare(game_manager)
                
    def update(self):
        self._player.handle_input()

    def draw(self, screen: Surface):
        screen.fill((0, 0, 0))
        self._player.draw(screen)
        
        for block in self._blocks:
            screen.blit(block.image, block.position)