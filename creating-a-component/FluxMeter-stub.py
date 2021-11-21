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
    By studying the Acme code, you can determine that a certain port number
    on an Analog-to-Digital-Converter (ADC) chip is used to distinguish
    between the left and right FluxMeter.    The left flux meter is connected to port
    number 3 on the ADC, and the right is connected to port 4.
    So, you can use the same values when creating the FluxMeter, and then
    use them to read from the correct ADC port that connects to desired
    Acme fm2319.

    Note that the code that you write, and even the code that you use might
    have almost nothing to do with the fm2319 chip.

    This is because the Pi uses a certain set of pins to connect over
    what is called an I2C bus.    It uses the I2C bus to send commands to
    the ADC chip to read the voltage level on a particular port, and maybe
    scales it accordingly.     The voltage level on a particular port is
    determined by the fm2319 chip that is connected to the port,
    but the Pi does not communicate with the fm2319 chip directly.
    """
    LEFT_PORT = 3
    RIGHT_PORT = 4

    def __init__(self, port_number):
        pass

    def getFlux(self):
        """
        Return a value of the proper type, even in a stub.
        """
        return 0.0

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



