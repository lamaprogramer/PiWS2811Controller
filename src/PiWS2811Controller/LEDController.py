import neopixel

from PiWS2811Controller.plugin import PluginManager
from PiWS2811Controller.plugin import Plugin
from PiWS2811Controller.theme.Theme import Theme

class LEDController:
    
    def __init__(self, pin, pixelCount, pixelOrder, pluginFolder):
        self.pixels: neopixel.NeoPixel = neopixel.NeoPixel(pin, pixelCount, auto_write=False, pixel_order=pixelOrder)
        self.pluginManager: PluginManager.PluginManager = PluginManager.PluginManager(pluginFolder)

        
    def runTheme(self, plugin: Plugin.Plugin, theme: Theme):
        self.runThemeWithPattern(plugin, theme.pattern, theme)
        
    def runThemeWithPattern(self, plugin: Plugin.Plugin, pattern: str, theme: Theme):
        plugin.patternManager.get(pattern).pattern(self.pixels, self.pixels.n, theme)
