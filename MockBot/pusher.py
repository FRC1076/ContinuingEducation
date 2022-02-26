import wpilib
import Enum


class JSStates(Enum):
    AButtonPressed = "AButtonPressed",


class Pusher:
    def __init__(self, dub_sol):
        self.piston = sub_sol
        self.piston.set(kOff)
        
    def pushOut(self):
        self.piston.set(kForward)

    def pullBack(self):
        self.piston.set(kReverse)

    
if __name__ == "__main__":
    """
    
    """
    js_events = { 1 : ("AButtonPressed",),   10 : ("AButtonPressed","BButtonPressed"),    13 : ("AButtonPressed", ) }


class MockJS:
    """
    Joystick with preloaded or forced events
    """
    def __init__(self, port_number, events):
        self.events = events
        self.event = None
        self.loop_index = 0

    def force_event(self, event)
        self.event = event

    def periodic(self):
        try:
            self.event = events[self.loop_index]
        except IndexError:
            self.event = ()
        self.loop_index = self.loop_index + 1

    def getAButtonPressed(self):
        return "AButtonPressed" in self.event

    def getBButtonPressed(self):
        return "BButtonReleased" in self.event


class MockDS:
    """
    MockDS takes a certain number of robot cycles to set or reset
    """
    def __init__(self, can_id, model, fwd_chan, rev_chan):
        self.state = kOff
        self.position = 0

    def set(self, state):
        self.state = state

    def get(self, state):
        return self.state


from robot import MyRobot

class MockRobot(MyRobot):

    def __init__(self):
        self.driver = MockJS(js_events)
        self.pusher = Pusher()



#
#   The actual test will create a Mock robot, initialize it with
#   mock components, and then do a periodic loop to test the teleop
#   function associated with the component.
#

mockds = MockDS(0, 0, 0, 0)
pusher = Pusher(mockds)

assert(pusher.state == kOff)

pusher.push()
assert(pusher.state == kForward)



robot = MockRobot()

loop = 0

while loop < 100:
    robot.driver.periodic()   # load the events for the current loop

    robot.teleopPusher()

    if robot.driver.getAButtonPressed()

        
    

    


        
