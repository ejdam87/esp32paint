from joystick import Joystick
from led_driver import Max7219

def inbound( x: int, y: int, board: Max7219 ) -> bool:
   return 0 <= x < board.width and 0 <= y < board.height

class Tracer:

    def __init__( self,
                  board: Max7219,
                  js: Joystick,
                  invert: bool=True ) -> None:

        self.board = board
        self.js = js
        self.invert = invert

    def update_pos( self, x: int, y: int ) -> None:
        self.js.update( )

        nx = x
        ny = y

        treshold = -0.5 if self.invert else 0.5

        if self.js.dx == treshold:
            nx += 1
        elif self.js.dx == -treshold:
            nx -= 1

        if self.js.dy == treshold:
            ny += 1
        elif self.js.dy == -treshold:
            ny -= 1

        if 0 <= nx < self.board.width:
            x = nx

        if 0 <= ny < self.board.height:
            y = ny

        return x, y

    def dot_trace( self ) -> None:

        x = y = 0

        while True:

            self.board.fill( 0 )
            self.board.pixel( x, y, 1 )
            self.board.show( )

            x, y = self.update_pos( x, y )


