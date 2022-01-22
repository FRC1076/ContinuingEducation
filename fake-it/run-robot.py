#
#  Run this program to see how the robot program fits together
#  Sometimes you just have to fake it!
#

class FakeGyro:

    default_fake_yaw_data = [ 0, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0 ]

    def __init__(self, fake_yaw_data = default_fake_yaw_data):
        """
        Pass a list of yaw readings to act as the yaw data.
        Pass nothing for the default data.
        """
        self.yaw_data = fake_yaw_data

    def getYaw(self):
        """
        Get and return the next piece of yaw data.
        Return 0 when it is done.
        """
        try:
            yaw = self.yaw_data.pop()
        except IndexError:
            yaw = 0
        return yaw


class FixedSpeedJoystick:

    def __init__(self, speed):
        self.speed = speed

    def getStick(self):
        return self.speed




class FakeDriveTrain:

    def __init__(self, left_motor, right_motor):
        self.left = left_motor
        self.right = right_motor

    def arcadeDrive(self, forward, rotate):
        """
        No physics here, just report how you are driving.
        """
        if rotate == 0:
            print("Driving STRAIGHT forward at speed: {}\n".format(forward))
        else:
            print("Driving forward: {}, rotating {}\n".format(forward, rotate))


class Robot:

    def __init__(self):

        self.driver = FixedSpeedJoystick(0.5)
        self.drivetrain = FakeDriveTrain("LEFT", "RIGHT")
        self.gyro = FakeGyro()


    def teleopPeriodic(self):

        # our setpoint is 0.  We want to drive straight
        setpoint = 0
        #  provide correction proportional to the departure from straight
        kP = 0.01

        # note that signs can always trip you up
        # Best to experiment to figure out exactly how it goes
        yaw = self.gyro.getYaw()
        error = setpoint - yaw
        correction = error * kP

        self.drivetrain.arcadeDrive(self.driver.getStick(), correction) 


if __name__ == "__main__":

    #
    #   Initialize the robot
    #
    myrobot = Robot()

    #
    #   Simulate the robot loop with 20 calls
    #
    for s in range(0, 20):
        print("Step {}:".format(s))
        myrobot.teleopPeriodic()

