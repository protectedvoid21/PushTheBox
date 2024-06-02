from dataclasses import dataclass

import pygame
from pygame import Vector2, Surface

import event_manager


@dataclass
class Button:
    _rect: pygame.Rect
    _text: str
    _font: pygame.font.Font
    _color: tuple[int, int, int]
    _actual_color: tuple[int, int, int]
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
        self._actual_color = color
        self._click_event = click_event

    def add_click_event(self, event: callable):
        self._click_event = event


    def update(self):
        self._actual_color = self._color
        
        if self.is_over(Vector2(pygame.mouse.get_pos())):
            self._actual_color = self._color[0] - 50, self._color[1] - 50, self._color[2] - 50
            
            if pygame.mouse.get_pressed()[0]:
                events = event_manager.EventManager.get_events()

                if pygame.MOUSEBUTTONDOWN in (event.type for event in events):
                    self._click_event()

    def draw(self, screen: Surface):
        pygame.draw.rect(screen, self._actual_color, self._rect)

        text = self._font.render(self._text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self._rect.center)
        screen.blit(text, text_rect)

    def is_over(self, pos: Vector2) -> bool:
        return self._rect.collidepoint(pos)