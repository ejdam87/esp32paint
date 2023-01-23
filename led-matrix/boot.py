from machine import Pin, SPI
from driver import Max7219

spi = SPI(1, baudrate=10000000)
screen = Max7219(32, 8, spi, Pin(15))
# screen.rect(0, 0, 32, 8, 1)  # Draws a frame
screen.text('', 1, 1, 1)
screen.show()
