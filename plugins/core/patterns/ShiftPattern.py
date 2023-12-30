import time

import PiWS2811Controller.tools.pattern.ColorPatterns as plugin

class ShiftPattern(plugin.ColorPattern):
    
    def pattern(self, pixels, pixelCount, theme):
        colors: list = theme.colors
        
        while True:
            for i in range(len(colors)):
                self.colorsWithShift(pixels, pixelCount, colors, i)
                time.sleep(theme.wait)

    def colorsWithShift(pixels, pixelCount: int, colors: list, shift: int):
        position = 0
        while position != pixelCount:
            for i in range(shift, len(colors)+shift):
                if position != pixelCount:
                    color = colors[i] if i < len(colors) else colors[i%len(colors)]
                    pixels[position] = color
                    position += 1
                else:
                    break
        pixels.show()