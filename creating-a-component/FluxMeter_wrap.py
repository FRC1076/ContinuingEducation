from ADC import *

class FluxMeter:
    """
    The FluxMeter wraps the Acme fm2319 to provide a simple
    interface that is more like what robot.py needs to use.    Recall
    that the FluxMeter is a sensor that measures etherial flux density
    on a scale of 0 to 1.0, but the fm2319 flux meter chip actually
    measures the flux on a scale from 0 to 5.0

    Usage:
        in robotInit, create the FluxMeter attached to the appropriate pin or port

                self.flux_left = FluxMeter(FluxMeter.LEFT_PORT)

        And in the main bodies of auton and teleop, you can use it to read
        ether flux density.

                lf = self.flux_left.getFlux()
                rf = self.flux_right.getFlux()
    """

    """
    The guiding principles when you wrap one service to create a new interface are:

         1. initialize the underlying service and save a handle to it
         2. save any other state during __init__ that are required to get
            the correct information from the underlying service

    Take a look at the ADC.py in this directory.    Some additional comments have
    been added to it to help you understand how it can be used.     Note that you
    can mostly figure out the minimum that you need to know by just looking at how
    it is being tested.
    """
    LEFT_PORT = 3
    RIGHT_PORT = 4

    def __init__(self, port_number):
        """
        Remember the port number for the adc receive
        Get a handle on the ADC to do the receive
        """
        self.port_number = port_number
        self.adc = Adc()

    def getFlux(self):
        """
        Use the wrapped adc device to get to the meter output
        """
        return self.adc.recvADC(self.port_number)

#
#  This "Dunder" (pythonista term derived from the double-underscores)
#  ensures the test code only runs when the file is run.
#         e.g.    python3 FluxMeter.py
#  If the file is imported, this stuff does not get executed.
#  So run it directly to test it out, and import it to use
#  the library.
#
#  NOTE:   This used Freenove library capabilities, so if you want
#  to test it, you'll want to run it on a Freenove robot.
#
if __name__ == "__main__":

    import time

    # robotInit
    fm_left = FluxMeter(FluxMeter.LEFT_PORT)
    fm_right = FluxMeter(FluxMeter.RIGHT_PORT)

    #
    # quasi periodic test (test 10 times with 1 second between)
    # This allows the tester to wave around the flux generator and
    # observe the changes
    for _ in range(10):
        print("Left :", fm_left.getFlux())
        print("Right :", fm_right.getFlux())
        time.sleep(1)



