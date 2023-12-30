from tools.theme import ThemeManager
from tools.pattern import PatternManager

class Plugin:

    def __init__(self, themeManager: ThemeManager.ThemeManager, patternManager: PatternManager.PatternManager):
        self.themeManager = themeManager
        self.patternManager = patternManager
