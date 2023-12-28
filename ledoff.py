import board
import neopixel

pin = board.D21
number_of_pixels = 50

pixels = neopixel.NeoPixel(pin, number_of_pixels, auto_write=False)

pixels.fill((0, 0, 0))
pixels.show()