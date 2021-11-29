class AnalogFluxMeter:
    """
    This software component reports the measured flux density on a scale
    from 0 to 1.0.

    Recall that the Acme Analog Flux Meter (afm2319), reports the instantaneous
    etherial flux density on a scale of 0 to 5.0 by reporting the value as an
    analog voltage on the same scale.   However, the Flux density as used in
    sensor applications has a maximum value of 1.0.    Thus, this component
    scales the reported value so it is in the proper range.

    Usage:
        in robotInit, create the AnalogFluxMeter attached to the appropriate Analog Input pin
(also referred to as a "channel" in the documentation.)

     https://robotpy.readthedocs.io/projects/wpilib/en/stable/wpilib/AnalogInput.html

     # Is a best practice to document how the robot is to be
     # wired based upon the contents of the robotInit().   So, make
     # sure is is clear in the creation of all of the components.
     # You should be able to deliver robotInit and the robot.config file
     # to electrical, and they ought to be able to read/understand it enough
     # to do all/most of the wiring.
     #
     # Why AnalogFluxMeter, instead of just FluxMeter?
     # Well, wpilib has examples of sensor components that use the same
     # naming conventions.  (e.g. AnalogGyro)  This distinguishes them
     # from Digital components that perform a similar function.   
     #
     ai_for_flux_left = wpilib.AnalogInput(2)
     self.flux_left = AnalogFluxMeter(ai_for_flux_left)

     And in the main bodies of auton and teleop, you can use it to read
     ether flux density.

          lf = self.flux_left.getFlux()
          rf = self.flux_right.getFlux()
    """
    def __init__(self, analog_input):
        """
        Requires a created AnalogInput object that is connected to the device
        """
        self.input = analog_input

    def getFlux(self):
        """
        Return the normalized (0 to 1.0) value of the Flux density
        """
        return self.input.getVoltage() / 5.0

#
#  This "Dunder" (pythonista term derived from the double-underscores)
#  ensures the code below only runs when the file is run directly.
#         e.g.    python3 FluxMeter.py
#  If the file is imported,
#         e.g.    import AnalogFluxMeter
#  the following code does not get run
#  
#  So run it directly to test it out, and import it to use
#  the library code above.
#
if __name__ == "__main__":

    import time
    #
    # Use stublib from this repo so this code can work
    # without requiring wpilib.   This is a trick you can
    # use when you want to develop your code isolated from
    # some software component.   AnalogInput is just a stub.
    # take a look at it in the stublib/AnalogInput.py file.
    #
    from stublib.AnalogInput import AnalogInput

    # robotInit
    fm_left_analog_input = AnalogInput(3)
    fm_left = AnalogFluxMeter(fm_left_analog_input)
    fm_right_analog_input = AnalogInput(4)
    fm_right = AnalogFluxMeter(fm_right_analog_input)

    #
    # quasi periodic test (test 10 times with 1 second between)
    # This allows the tester to wave around the flux generator and
    # observe the changes
    for _ in range(10):
        print("Left :", fm_left.getFlux())
        print("Right :", fm_right.getFlux())
        time.sleep(1)



