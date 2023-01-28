from machine import Pin, SPI
from micropython import const
import framebuf


## --- Constants
_DIGIT_0 = const( 0x1 )

_DECODE_MODE = const( 0x9 )
_NO_DECODE = const( 0x0 )

_INTENSITY = const( 0xA )
_INTENSITY_MIN = const( 0x0 )

_SCAN_LIMIT = const( 0xB )
_DISPLAY_ALL_DIGITS = const( 0x7 )

_SHUTDOWN = const( 0xC )
_SHUTDOWN_MODE = const( 0x0 )
_NORMAL_OPERATION = const( 0x1 )

_DISPLAY_TEST = const( 0xF )
_DISPLAY_TEST_NORMAL_OPERATION = const( 0x0 )

_MATRIX_SIZE = const( 8 )
## ---


class Max7219( framebuf.FrameBuffer ):
    """
    Driver for MAX7219 8x8 LED matrices
    """

    def __init__( self,
                  width: int,
                  height: int,
                  spi: SPI,
                  cs: Pin ) -> None:

        ## --- Pins setup
        self.spi = spi
        self.cs = cs
        self.cs.init( Pin.OUT, True )
        ## ---

        self.width = width
        self.height = height

        self.cols = width // _MATRIX_SIZE
        self.rows = height // _MATRIX_SIZE

        ## Number of 8x8 matrices
        self.nb_matrices = self.cols * self.rows

        ## 1 bit per pixel (on / off) -> 8 bytes per matrix
        self.buffer = bytearray( width * height // 8 )
        frame_format = framebuf.MONO_HLSB
        super( ).__init__( self.buffer, width, height, frame_format )

        self.init_display( )

    def _write_command( self, command: int, data: int ) -> None:
        """Write command on SPI ( for every matrix )"""
        cmd = bytearray( [ command, data ] )
        self.cs( 0 )
        for _ in range( self.nb_matrices ):
            self.spi.write( cmd )
        self.cs( 1 )

    def init_display( self ) -> None:
        """Init hardware"""
        for command, data in (
            ( _SHUTDOWN, _SHUTDOWN_MODE ),  # Prevent flash during init
            ( _DECODE_MODE, _NO_DECODE ),
            ( _DISPLAY_TEST, _DISPLAY_TEST_NORMAL_OPERATION ),
            ( _INTENSITY, _INTENSITY_MIN ),
            ( _SCAN_LIMIT, _DISPLAY_ALL_DIGITS ),
            ( _SHUTDOWN, _NORMAL_OPERATION ),
        ):
            self._write_command( command, data )

        self.fill( 0 )
        self.show( )

    def brightness( self, value: int ) -> None:
        """Set display brightness (0 to 15)"""
        if not 0 <= value < 16:
            raise ValueError( "Brightness must be between 0 and 15" )
        self._write_command( _INTENSITY, value )

    def show( self ) -> None:
        """Update display"""

        for line in range( 8 ): ## Every matrix has 8 rows
            self.cs( 0 )

            for matrix in range( self.nb_matrices ):
                # Guess where the matrix is placed
                row, col = divmod( matrix, self.cols )
                # Compute where the data starts
                offset = row * 8 * self.cols
                index = col + line * self.cols + offset

                self.spi.write( bytearray([_DIGIT_0 + line, self.buffer[index]]) )

            self.cs( 1 )
