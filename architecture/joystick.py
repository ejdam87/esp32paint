import machine

class Joystick:

    def __init__( self, vrx: int, vry: int, sw: int ) -> None:

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
