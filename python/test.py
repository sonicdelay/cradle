import time

from ..rpi_ws281x.python.neopixel import *
 
# LED strip configuration:
LED_COUNT      = 12     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10       # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 127     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.SK6812_STRIP_GRBW   # Strip type and colour ordering

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

# Intialize the library (must be called once before other functions).
strip.begin()

#for i in range(strip.numPixels()):
#    strip.setPixelColor(i, Color(255,0,0))
#
#strip.show()

RUN_COLORS = [
 (255,0,0),
 (0,255,0),
 (0,0,255),
 (255,0,0)
]
l = strip.numPixels()
lc = len(RUN_COLORS) - 1
bl = l / lc
while True:
    for startPos in range(l):
        for i in range(l):
            relPos = (i - startPos) % bl
            block = (i - startPos) // bl %lc 
            factors = (relPos * 1.0 / bl , (bl - relPos)*1.0 / bl)
            red = RUN_COLORS[block+1][0] * factors[0] + RUN_COLORS[block][0] * factors[1]
            green = RUN_COLORS[block+1][1] * factors[0] + RUN_COLORS[block][1] * factors[1]
            blue = RUN_COLORS[block+1][2] * factors[0] + RUN_COLORS[block][2] * factors[1]
            color = Color(int(red)*1 ,int(green/2)*1,int(blue)*1)
            strip.setPixelColor(i, color)
        strip.show()
        time.sleep(50/1000.0)
