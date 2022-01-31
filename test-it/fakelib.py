#
#   Fake library for subsystem unit testing
#
class FakeDoubleSolenoid():

    def __init__(self, fwd_port, rev_port):
        self.fp = fwd_port
        self.rp = rev_port
        self.state = 0

    def set(self, state):
        self.state = state

    def get(self):
        return self.state

class FakeMotorController():

    def __init__(self, can_id):
        self.cid = can_id
        self.speed = 0

    def set(self, speed):
        self.speed = speed

    def get(self):
        return self.speed
