import neopixel

from PiWS2811Controller.plugin import PluginManager
from PiWS2811Controller.plugin import Plugin
from PiWS2811Controller.theme.Theme import Theme

class LEDController:
    
    def __init__(self, pin, pixelCount, pixelOrder, pluginFolder):
        self.pixels: neopixel.NeoPixel = neopixel.NeoPixel(pin, pixelCount, auto_write=False, pixel_order=pixelOrder)
        self.pluginManager: PluginManager.PluginManager = PluginManager.PluginManager(pluginFolder)

        
    def runTheme(self, plugin: Plugin.Plugin, theme: Theme):
        if theme.pattern != "ANY":
            self.runThemeWithPattern(plugin, theme.pattern, theme)
        else:
            print("No pattern specified")
        
    def runThemeWithPattern(self, plugin: Plugin.Plugin, pattern: str, theme: Theme):
        if theme.pattern == "ANY":
            plugin.patternManager.get(pattern).pattern(self.pixels, self.pixels.n, theme)
        else:
            print("Theme already has a specified pattern")
