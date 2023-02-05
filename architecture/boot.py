from machine import Pin, SPI
from led_driver import Max7219
from joystick import Joystick
import tracer


WIDTH = 32
HEIGHT = 8

CS_PIN = Pin( 15 )

spi = SPI( 1, baudrate=10000000 )
screen = Max7219( 32, 8, spi, CS_PIN )

j = Joystick( 34, 35, 17 )

def observe( j: Joystick ) -> None:

    j.update()
    print( j.dx, j.dy )

t = tracer.Tracer( screen, j )
