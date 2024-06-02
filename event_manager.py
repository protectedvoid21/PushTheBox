from dataclasses import dataclass

import pygame
from pygame.event import Event

class EventManager:
    _events: list[Event] = []
    
    @staticmethod
    def update():
        _events: list[Event] = pygame.event.get()
        EventManager._events = _events
        
    @staticmethod
    def get_events() -> list[Event]:
        return EventManager._events