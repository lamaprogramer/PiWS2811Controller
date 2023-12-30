import neopixel
import os

from core import util
from tools.plugin import PluginManager

class LEDController:
    def __init__(self, pin, pixelCount):
        self.pin = pin
        self.pixelCount = pixelCount

        print(util.PARENT_FOLDER)

        self.pixels: neopixel.NeoPixel = neopixel.NeoPixel(pin, pixelCount, auto_write=False)
        self.pluginManager: PluginManager.PluginManager = PluginManager.PluginManager(os.path.join(util.PARENT_FOLDER, "plugins"))