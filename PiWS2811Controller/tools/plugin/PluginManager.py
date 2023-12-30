import os


from tools.plugin import Plugin
from tools.theme import ThemeManager
from tools.pattern import PatternManager

class PluginManager:

    def __init__(self, pluginsPath):

        pluginNames = []
        
        for (dirpath, dirnames, filenames) in os.walk(pluginsPath):
            pluginNames.extend(dirnames)
            break
        
        self.plugins = []
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
            
            self.plugins.append(Plugin.Plugin(themeManager, patternManager))


