from dataclasses import dataclass

import pygame
from pygame import Vector2, Surface

from game_time import GameTime


@dataclass
class Button:
    _rect: pygame.Rect
    _text: str
    _font: pygame.font.Font
    _color: tuple[int, int, int]
    _click_event: callable = None

    def __init__(self, rect: tuple[int, int, int, int],
                 text: str,
                 click_event: callable,
                 font: pygame.font.Font = None,
                 color: tuple[int, int, int] = (255, 255, 255)):
        self._rect = pygame.rect.Rect(rect)
        self._text = text
        self._font = font or pygame.font.Font(None, 32)
        self._color = color
        self._click_event = click_event

    def add_click_event(self, event: callable):
        self._click_event = event


    def update(self):
        if self.is_over(Vector2(pygame.mouse.get_pos())):
            if pygame.mouse.get_pressed()[0]:
                if pygame.event.get(pygame.MOUSEBUTTONUP):
                    self._click_event()

    def draw(self, screen: Surface):
        pygame.draw.rect(screen, self._color, self._rect)

        text = self._font.render(self._text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self._rect.center)
        screen.blit(text, text_rect)

    def is_over(self, pos: Vector2) -> bool:
        return self._rect.collidepoint(pos)