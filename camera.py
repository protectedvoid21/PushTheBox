import pygame
from pygame import Vector2


class Camera:
    """
    Represents the camera in the game.

    Attributes:
        camera (pygame.Rect): The rectangle representing the camera's position and size.
        width (int): The width of the camera.
        height (int): The height of the camera.
    """


    def __init__(self, width: int, height: int):
        """
        Initialize the Camera with the given width and height.

        Args:
            width (int): The width of the camera.
            height (int): The height of the camera.
        """
        self.camera = pygame.Rect(0, 0, width, height)
        self.width: int = width
        self.height: int = height


    def apply(self, entity_rect: pygame.Rect) -> pygame.Rect:
        """
        Apply the camera to the given entity.

        This method should be called to get the position of the entity relative to the camera.

        Args:
            entity_rect (pygame.Rect): The rectangle representing the entity's position and size.

        Returns:
            pygame.Rect: The rectangle representing the entity's position and size relative to the camera.
        """
        return entity_rect.move(self.camera.topleft)


    def update(self, target_rect: pygame.Rect):
        """
        Update the camera.

        This method should be called once per frame. It updates the camera's position to follow the target.

        Args:
            target_rect (pygame.Rect): The rectangle representing the target's position and size.
        """
        x = -target_rect.centerx + self.width // 2
        y = -target_rect.centery + self.height // 2

        self.camera = pygame.Rect(x, y, self.width, self.height)