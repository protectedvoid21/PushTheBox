import pygame
from pygame import Vector2


class Camera:
    def __init__(self, width: int, height: int):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width: int = width
        self.height: int = height

    def apply(self, entity_rect: pygame.Rect) -> pygame.Rect:
        return entity_rect.move(self.camera.topleft)

    def update(self, target_rect: pygame.Rect):    
        x = -target_rect.centerx + self.width // 2
        y = -target_rect.centery + self.height // 2
        
        self.camera = pygame.Rect(x, y, self.width, self.height)