from PiWS2811Controller.pattern.ColorPatterns import ColorPattern, loadPatterns
from typing import Type, List


class PatternManager:

    def __init__(self, path):
        self.patterns: List[Type[ColorPattern]] = loadPatterns(path)
        print("returned plugins: " + str(self.patterns))
        
    def get(self, name: str) -> Type[ColorPattern]:
        for plugin in self.patterns:
            inst = plugin()
            if inst.__class__.__name__ == name:
                return inst
    