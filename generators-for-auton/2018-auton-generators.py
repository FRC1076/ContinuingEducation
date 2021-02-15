import time

class drivetrain:
    """
    This dummy drivetrain does not really drive, but that
    works out okay for learning.
    """
    def __init__(self):
        pass

    def arcadeDrive(self, forward, rotate):
        print("Driving forward {} rotating {}".format(forward, rotate))
    
    def stop(self):
        print("STOPPED Driving")


class BaseAutonomous:
    def init(self):
        """
        Init method is called at the very start of the auton task.
        Use it to set start conditions, calculate end time, etc...
        Always return this object
        """
        return self

    def execute(self):
        pass

    def end(self):
        pass

    def run(self):
        """
        Define a function to yield and then end, so we
        can return a generator.
        So run() always does an init, then it returns a generator
        that does all of the execute() and then the end().
        """
        def _execute():
            yield from self.execute()
            self.end()
        self.init()
        return _execute()

class Timed(BaseAutonomous):
    """
    Takes an auton task and a duration as argument
    Runs the auton task until it either ends or until
    the duration time ends.
    """
    def __init__(self, auto, duration):
        self.auto = auto
        self.duration = duration

    def init(self):
        self.auto.init()
        self.end_time = time.time() + self.duration

    def execute(self):
        """
        Run the task execution steps until it ends (stops
        iteration)
        Otherwise, check if it has run out of time and
        break out of the loop.
        """
        for _ in self.auto.execute():
            if time.time() > self.end_time:
                break
            yield

    def end(self):
        self.auto.end()


class ArcadeDriveDeadReckon(BaseAutonomous):
    """
    Drive with the specified forward and rotate settings
    """
    def __init__(self, drivetrain, forward, rotate):
        self.drivetrain = drivetrain
        self.forward = forward
        self.rotate = rotate

    def init(self):
        """
        Initially we are stopped.
        """
        self.drivetrain.stop()

    def execute(self):
        """
        Drive for the next cycle and yield to the caller.
        This *could* go on forever if the caller does not stop (Timed() does)
        We *could* end this outselves, though, if we detect that we
        are close to a target, or if we just bumped into something.
        """
        while True:
            self.drivetrain.arcadeDrive(self.forward, self.rotate)
            yield

    def end(self):
        self.drivetrain.stop()
    

"""
Put auton generators in this function, one after another
This function will be used to create the generator for all
of them in sequence.
"""
def robotAuton(train):
    # Drive forward at 50% power for 5 seconds
    yield from Timed(ArcadeDriveDeadReckon(train, forward=0.5, rotate=0), duration=5).run()
    # Rotate at 10% power for 3 seconds
    yield from Timed(ArcadeDriveDeadReckon(train, forward=0, rotate=0.1), duration=3).run()

    
print("Create the drivetrain")
# create the drivetrain for auton to use
dt = drivetrain()
# create the generator that generates auton steps
auton = robotAuton(dt)

"""
For learning purposes each robot step is 1 second long.
Since this is auton, we'll give it 15 steps.
"""
start_time = time.time()
for step in range(0,15):
    print("Robot loop {} time {}".format(step, round(time.time() - start_time, 1)))

    """
    Do the next step according to auton generator
    """
    try:
        next(auton)
    except:
        dt.stop()

    time.sleep(1)