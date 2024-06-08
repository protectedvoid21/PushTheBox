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
    _image: pygame.image = None
    _click_event: callable = None

    def __init__(self, rect: tuple[int, int, int, int],
                 click_event: callable = None,
                 text: str = None,
                 font: pygame.font.Font = None,
                 color: tuple[int, int, int] = (255, 255, 255),
                 image: pygame.image = None):
        self._rect = pygame.rect.Rect(rect)
        self._text = text
        self._font = font or pygame.font.Font(None, 32)
        self._color = color
        self._actual_color = color
        self._image = image
        if self._image:
            self._image = pygame.transform.scale(self._image, (self._rect.width, self._rect.height))
        self._click_event = click_event

    def add_click_event(self, event: callable):
        self._click_event = event


    def update(self):
        self._actual_color = self._color
        
        if self.is_over(Vector2(pygame.mouse.get_pos())):
            self._actual_color = self._color[0] - 50, self._color[1] - 50, self._color[2] - 50            
            if self._click_event and pygame.mouse.get_pressed()[0]:
                events = event_manager.EventManager.get_events()
                if pygame.MOUSEBUTTONDOWN in (event.type for event in events):
                    self._click_event()

    def draw(self, screen: Surface):
        if self._image:
            screen.blit(self._image, self._rect)
        else:
            pygame.draw.rect(screen, self._actual_color, self._rect)

        text = self._font.render(self._text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self._rect.center)
        screen.blit(text, text_rect)

    def is_over(self, pos: Vector2) -> bool:
        return self._rect.collidepoint(pos)