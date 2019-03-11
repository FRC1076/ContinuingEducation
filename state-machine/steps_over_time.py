import wpilib
from time import sleep
from enum import Enum

class StepsOverTime:  
    INITIALIZED = 0
    ACTIVATED = 1
    THREEING = 2
    DONE = 3

    def __init__(self):
        self.state = StepsOverTime.INITIALIZED

    def isInitialized(self):
        return self.state == StepsOverTime.INITIALIZED

    def activate(self):
        """
        Only activate if in the INITIALIZED state
        """
        if self.state == StepsOverTime.INITIALIZED:
            self.stepCount = 0
            self.timer = wpilib.Timer()
            self.timer.start()
            self.state = StepsOverTime.ACTIVATED
   
    def nextStep(self):
        """
        Take a single step and do what the state, stepCount, or
        time requires.
        """
        self.stepCount += 1

        if self.stepCount == 5:
            print("Do that thing 5 loops later")
            self.state = StepsOverTime.THREEING

        if self.state == StepsOverTime.THREEING and (self.stepCount % 3) == 0:
            print("Multiple of 3 after 5")

        if self.timer.hasPeriodPassed(8):
            print("Do that thing that you want to do 8 seconds after activation")
            self.state = StepsOverTime.DONE

        if self.state == StepsOverTime.DONE:
            print("Leave me alone, will you?")
        

def activatingEvent():
    return True

def run_example():

    # Initialization
    sot = StepsOverTime()

    # pretend this is a robot loop that runs only 11 times
    for _ in range(11):

        # Some event activates the state machine
        if activatingEvent() and sot.isInitialized():
            sot.activate()

        # In each loop, tell the state machine to take a step
        sot.nextStep()
        sleep(1)

if __name__ == '__main__':
    run_example()




