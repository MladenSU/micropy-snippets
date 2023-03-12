from machine import Pin, SPI
from ssd1306 import SSD1306_SPI
import sys


class DisplayManager:
    def __init__(self, dcPin: int, resPin: int, csPin: int, mosiPin: int, sckPin: int, spiType: int = 0,
                 resolution: tuple = (128, 64)):
        spi = SPI(spiType, 100000, mosi=Pin(mosiPin), sck=Pin(sckPin))
        self.display = SSD1306_SPI(resolution[0], resolution[1], spi, Pin(dcPin), Pin(resPin), Pin(csPin))

    def displayOnScreen(self, text: list):
        """The function accept a list of maximum 6 indexes.
        The reason for that is that each index will be printed on separate line
        on 128x64 SPI display, the limit is 6 lines and 16 chars per line."""
        pos = 0
        if not isinstance(text, list) or len(text) > 6:
            self.display.text("Too long or not", 0, 0)
            self.display.text("correct format!", 0, 11)
            self.display.show()
            sys.exit(1)

        for line in text:
            self.display.text(line, 0, pos)
            pos += 11

        self.display.show()


# Example
test = DisplayManager(dcPin=17, resPin=20, csPin=16, mosiPin=19, sckPin=18)
test.displayOnScreen(["Status:", "Loading", "", "IP Addr:", "123.123.123.123"])