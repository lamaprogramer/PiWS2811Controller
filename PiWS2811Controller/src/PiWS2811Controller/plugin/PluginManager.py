import os
import neopixel

from PiWS2811Controller.plugin import Plugin
from PiWS2811Controller.theme import ThemeManager
from PiWS2811Controller.pattern import PatternManager
from PiWS2811Controller.theme.Theme import Theme

class PluginManager:

    def __init__(self, pluginsPath: str):
        self.plugins = {}
        pluginNames = []
        
        for (dirpath, dirnames, filenames) in os.walk(pluginsPath):
            pluginNames.extend(dirnames)
            break
        
        for pluginName in pluginNames:
            pluginDir = os.path.join(pluginsPath, pluginName)

            themesPath = os.path.join(pluginDir, "themes")
            patternsPath = os.path.join(pluginDir, "patterns")

            themeManager = None
            patternManager = None
            if os.path.exists(themesPath):
                themeManager = ThemeManager.ThemeManager(themesPath)

            if os.path.exists(patternsPath):
                patternManager = PatternManager.PatternManager(patternsPath)
            
            self.plugins[pluginName] = Plugin.Plugin(pluginName, themeManager, patternManager)
    

