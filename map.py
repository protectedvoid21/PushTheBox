from dataclasses import dataclass

from block import Block


@dataclass
class Map:
    _blocks: list[Block]
    
    def __init__(self, json_data: dict):
        self._data = json_data
        
    def load(self):
        for block in self._data['blocks']:
            self._blocks.append(Block(block['img'], block['position']))