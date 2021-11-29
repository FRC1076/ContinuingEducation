from ADC import *


class AnalogInput:
    """
    Ports on the Analog-to-digital converter chip could be treated
    as AnalogInput pins.   Then, they can be put together just
    like the wpilib implementation does.

    The guiding principles when you wrap one service to create a new interface are:

         1. initialize the underlying service and save a handle to it
         2. save any other state during __init__ that is required to get
            the correct information from the underlying service

    Take a look at the ADC.py in this directory.    Some additional comments have
    been added to it to help you understand how it can be used.     Note that you
    can mostly figure out the minimum that you need to know by just looking at how
    it is being tested.
    """
    def __init__(self, port_number):
        self.port_number = port_number
        self.adc = Adc()

    def getVoltage(self):
        return self.adc.recvADC(self.port_number)
        

class AnalogFluxMeter:
    """
    AnalogFluxMeter reads the value of the 

    Usage:
        in robotInit, create the FluxMeter attached to the appropriate pin or port

                self.flux_left = FluxMeter(FluxMeter.LEFT_PORT)

        And in the main bodies of auton and teleop, you can use it to read
        ether flux density.

                lf = self.flux_left.getFlux()
                rf = self.flux_right.getFlux()

    The guiding principles when you wrap one service to create a new interface are:

         1. initialize the underlying service and save a handle to it
         2. save any other state during __init__ that is required to get
            the correct information from the underlying service

    Take a look at the ADC.py in this directory.    Some additional comments have
    been added to it to help you understand how it can be used.     Note that you
    can mostly figure out the minimum that you need to know by just looking at how
    it is being tested.

    Because the Freenove is hard-wired, we cannot chose where the Flux Meter is
    connected, so we record the port numbers here so that they are known when
    the appropriate connection is needed.
    """
    LEFT_PORT = 3
    RIGHT_PORT = 4

    def __init__(self, analog_input):
        """
        Use the analog_input to get to the Flux Meter output
        """
        self.input = analog_input

    def getFlux(self):
        """
        Return the normalized Flux value (range 0 to 1.0)
        """
        return self.input.getVoltage / 5.0

#
#  This "Dunder" (pythonista term derived from the double-underscores)
#  ensures the test code only runs when the file is run.
#         e.g.    python3 FluxMeter.py
#  If the file is imported, this stuff does not get executed.
#  So run it directly to test it out, and import it to use
#  the library.
#
if __name__ == "__main__":

    import time

    # robotInit
    ai_flux_left = AnalogInput(FluxMeter.LEFT_PORT)
    fm_left = FluxMeter(ai_flux_left)
    ai_flux_right = AnalogInput(FluxMeter.RIGHT_PORT)
    fm_right = FluxMeter(ai_flux_right)

    #
    # quasi periodic test (test 10 times with 1 second between)
    # This allows the tester to wave around the flux generator and
    # observe the changes
    for _ in range(10):
        print("Left :", fm_left.getFlux())
        print("Right :", fm_right.getFlux())
        time.sleep(1)



