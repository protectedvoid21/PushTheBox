from dataclasses import dataclass

import pygame
from pygame.event import Event

class EventManager:
    """
        Manages the events in the game globally.
        
        This class is a singleton and should not be instantiated except of GameManager.
        
        To get the current events, use EventManager.get_events().
    """
    _events: list[Event] = []
    
    @staticmethod
    def update():
        """
            Update the list of current events.
    
            This method should be called once per frame.
        """
        _events: list[Event] = pygame.event.get()
        EventManager._events = _events
        
    @staticmethod
    def get_events() -> list[Event]:
        """
            Get the list of current events.
    
            Returns:
                list[Event]: The current events.
        """
        return EventManager._events