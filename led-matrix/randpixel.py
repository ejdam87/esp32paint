## Program which randomly toggle particular pixels

from driver import Max7219
from random import random

ON = 1
OFF = 0

def pixel_storm( screen: Max7219 ) -> None:

    while True:
        for x in range( screen.width ):
            for y in range( screen.height ):

                if random( ) >= 0.5:    ## 50% chance
                    screen.pixel( x, y, ON )
                else:
                    screen.pixel( x, y, OFF )

        screen.show( )
