from machine import Pin, SPI
from driver import Max7219

## dimensions of my matrix
WIDTH = 32
HEIGHT = 8

CS_PIN = Pin( 15 )

spi = SPI( 1, baudrate=10000000 )
screen = Max7219( 32, 8, spi, CS_PIN )
