import board
import sys
from pathlib import Path

from core.LEDController import LEDController

from tools.plugin.Plugin import Plugin
from tools.theme.Theme import Theme

if __name__ == "__main__":
    controller: LEDController = LEDController(board.D21, 50)

    plugin: Plugin = controller.pluginManager.plugins["core"]

    theme: Theme = plugin.themeManager.themes[0]
    plugin.patternManager.get("ShiftPattern").pattern(controller.pixels, controller.pixelCount, theme)


#fade(theme.colors, theme.wait, theme.speed, theme.steps)

# previousColor = (0, 0, 0)
# while True:
#     red = random.randint(0, 255)
#     green = random.randint(0, 255)
#     blue = random.randint(0, 255)

#     fadeToColor(previousColor, (red, green, blue), 1, 25)
#     previousColor = (red, green, blue)

#     #pixels[i] = (red, green, blue)
#     #time.sleep(1)