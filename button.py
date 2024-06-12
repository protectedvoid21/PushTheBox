from dataclasses import dataclass

import pygame
from pygame import Vector2, Surface

import event_manager

@dataclass
class Button:
    """
    Class representing a button in the game.
    
    Button can have a text, image, and a click event.
    """
    _rect: pygame.Rect
    _text: str
    _font: pygame.font.Font
    _current_rect: pygame.Rect
    _color: tuple[int, int, int]
    _actual_color: tuple[int, int, int]
    _image: pygame.image = None
    _click_event: callable = None
    _is_hovered: bool = False


    def __init__(self, rect: tuple[int, int, int, int],
                 click_event: callable = None,
                 text: str = '',
                 font: pygame.font.Font = None,
                 color: tuple[int, int, int] = (255, 255, 255),
                 image: pygame.image = None):
        """
        Initialize the Button with the given rectangle, click event, text, font, color, and image.

        Args:
            rect (tuple[int, int, int, int]): The rectangle representing the button's position and size.
            click_event (callable): The event that occurs when the button is clicked.
            text (str): The text on the button.
            font (pygame.font.Font): The font of the text.
            color (tuple[int, int, int]): The color of the button.
            image (pygame.image): The image of the button.
        """
        self._rect = pygame.rect.Rect(rect)
        self._current_rect = self._rect
        self._text = text.upper()
        self._font = font or pygame.font.Font(None, 60)
        self._color = color
        self._actual_color = color
        self._image = image
        if self._image:
            self._image = pygame.transform.scale(self._image, (self._rect.width, self._rect.height))
        self._click_event = click_event


    def add_click_event(self, event: callable):
        """
        Add a click event to the button.

        Args:
            event (callable): The event to add.
        """
        self._click_event = event


    @property
    def rect(self) -> pygame.Rect:
        """
        Get the rectangle representing the button's position and size.

        Returns:
            pygame.Rect: The rectangle representing the button's position and size.
        """
        return self._rect


    def hover_effect(self, surface) -> pygame.image:
        """
        Get the hover effect for the button.

        Args:
            surface (pygame.Surface): The surface to apply the hover effect to.

        Returns:
            pygame.image: The image with the hover effect applied.
        """
        return pygame.transform.scale(surface, (self._rect.width + 10, self._rect.height + 10))


    def update(self):
        """
         Update the button.

         This method should be called once per frame. It updates the color and rectangle of the button based on whether it is being hovered over.
         """
        self._actual_color = self._color
        self._current_rect = self._rect
        
        self._is_hovered = self.is_over(Vector2(pygame.mouse.get_pos()))

        if self._is_hovered:
            if self._click_event and pygame.mouse.get_pressed()[0]:
                events = event_manager.EventManager.get_events()
                if pygame.MOUSEBUTTONDOWN in (event.type for event in events):
                    self._click_event()

            

    def draw(self, screen: Surface):
        """
        Draw the button on the screen.

        Args:
            screen (Surface): The game screen.
        """
        if self._image:
            if self._is_hovered:
                offset_rect = self._current_rect.inflate(10, 10)
                screen.blit(self.hover_effect(self._image), offset_rect)
            else:
                screen.blit(self._image, self._current_rect)
        else:
            pygame.draw.rect(screen, self._actual_color, self._current_rect)

        text = self._font.render(self._text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self._rect.center)
        screen.blit(text, text_rect)


    def is_over(self, pos: Vector2) -> bool:
        """
        Check whether the button is being hovered over.

        Args:
            pos (Vector2): The position of the mouse.

        Returns:
            bool: Whether the button is being hovered over.
        """
        return self._rect.collidepoint(pos)
