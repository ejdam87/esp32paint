import machine

class Joystick:

    # Maximum voltage produced by joystick
    ceiling = 4095

    # ( Average ) Voltage rate of joystick located in the middle
    x_center = 1963
    y_center = 1968

    def __init__( self, vrx: int, vry: int, sw: int ) -> None:

        ## represents current joystick offset ( number between -0.5 and 0.5 )
        self.dx = 0
        self.dy = 0

        ## represents whether joystick button is currently clicked
        self.button = 1

        ## Setup analog-digital convertion on vrx and vry pins
        self.jx = machine.ADC( machine.Pin( vrx ) )
        self.jy = machine.ADC( machine.Pin( vry ) )

        ## Set precision
        self.jx.width( machine.ADC.WIDTH_12BIT )
        self.jy.width( machine.ADC.WIDTH_12BIT )

        ## Allow higher range of input voltage
        self.jx.atten( machine.ADC.ATTN_11DB )
        self.jy.atten( machine.ADC.ATTN_11DB )

        self.js = machine.Pin( sw, machine.Pin.IN, machine.Pin.PULL_UP )

    def is_pressed( self ) -> bool:
        return not self.button

    def update( self ) -> None:
        jx = self.jx.read( )
        jy = self.jy.read( )

        self.button = self.js.value( )

        self.dx = ( jx - Joystick.x_center ) / Joystick.ceiling
        self.dy = ( jy - Joystick.y_center ) / Joystick.ceiling
        self.dx = round( self.dx, 1 )
        self.dy = round( self.dy, 1 )

