import time
import tools.pattern.ColorPatterns as plugin

class FadePattern(plugin.ColorPattern):
    
    def pattern(self, pixels, pixelCount, theme):
        colors: list = theme.colors
        
        
        while True:
            for i in range(len(colors)):
                #print(colors[i])
                nextColor = colors[i+1] if i+1 < len(colors) else colors[0]
                self.lerpColor(pixels, colors[i], nextColor, theme.speed, theme.steps)
                time.sleep(theme.wait)

    def lerpColor(self, pixels, currentColor, newColor, speed, steps):
        redDifference = newColor[0] - currentColor[0]
        greenDifference = newColor[1] - currentColor[1]
        blueDifference = newColor[2] - currentColor[2]

        pixelsFromLeft = 0
        inbetweenColor = [0, 0, 0]
        while pixelsFromLeft <= 1.0:

            # y = mx + b
            inbetweenColor[2] = int(redDifference * pixelsFromLeft + currentColor[0])
            inbetweenColor[1] = int(greenDifference * pixelsFromLeft + currentColor[1])
            inbetweenColor[0] = int(blueDifference * pixelsFromLeft + currentColor[2])

            #print(str(inbetweenColor) + " : " + str(newColor))
            pixels.fill(inbetweenColor)
            pixels.show()
            
            pixelsFromLeft += 1/steps
            time.sleep(speed/steps)