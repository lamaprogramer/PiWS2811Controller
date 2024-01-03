from PiWS2811Controller.theme import ThemeManager
from PiWS2811Controller.pattern import PatternManager

class Plugin:

    def __init__(self, pluginName: str, themeManager: ThemeManager.ThemeManager, patternManager: PatternManager.PatternManager):
        self.pluginName = pluginName
        self.themeManager = themeManager
        self.patternManager = patternManager
