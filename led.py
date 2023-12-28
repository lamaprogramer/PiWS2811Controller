import board
import neopixel
import random
import time

from ThemeManager import ThemeManager
from Theme import Theme

pin = board.D21
number_of_pixels = 50

pixels = neopixel.NeoPixel(pin, number_of_pixels, auto_write=False)


def fadeToColor(currentColor, newColor, speed, steps):
    redDifference = newColor[0] - currentColor[0]
    greenDifference = newColor[1] - currentColor[1]
    blueDifference = newColor[2] - currentColor[2]

    pixelsFromLeft = 0
    inbetweenColor = (0, 0, 0)
    while pixelsFromLeft <= 1.0:
        red = int(currentColor[0] + redDifference * pixelsFromLeft)
        green = int(currentColor[1] + greenDifference * pixelsFromLeft)
        blue = int(currentColor[2] + blueDifference * pixelsFromLeft)

        inbetweenColor = (red, green, blue)

        print(str(inbetweenColor) + " : " + str(newColor))
        pixels.fill(inbetweenColor)
        pixels.show()
        
        pixelsFromLeft += 1/steps
        time.sleep(speed/steps)

def fade(colors: list, wait: float, speed: float, steps: int):
    while True:
        for i in range(len(colors)):
            nextColor = colors[i+1] if i+1 < len(colors) else colors[0]
            fadeToColor(colors[i], nextColor, speed, steps)
            time.sleep(wait)

themeManager = ThemeManager()

theme: Theme = themeManager.themes[0]
fade(theme.colors, theme.wait, theme.speed, theme.steps)

# previousColor = (0, 0, 0)
# while True:
#     red = random.randint(0, 255)
#     green = random.randint(0, 255)
#     blue = random.randint(0, 255)

#     fadeToColor(previousColor, (red, green, blue), 1, 25)
#     previousColor = (red, green, blue)

#     #pixels[i] = (red, green, blue)
#     #time.sleep(1)