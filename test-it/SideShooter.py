
from wpilib import DoubleSolenoid

from robotmap import SHOOTER_ID
from robotmap import SIDEARM_FWD_PORT,  SIDEARM_REVERSE_PORT
from robotmap import SHOOTER_DEFAULT_SHOT_SPEED

# shorthands
kOff = DoubleSolenoid.Value.kOff
kForward = DoubleSolenoid.Value.kForward
kReverse = DoubleSolenoid.Value.kReverse

class SideArmShooter:
    '''
    Sidearm shooter leans out and then shoots to get past
    potentially blocking opponent.  Pneumatics control the
    lean, and a motor spins to the specified speed to eject
    the projectile.

    To simplify building the user interface, we just provide
    operations for each step in succession.
    '''
    
    def __init__(self, sidearm, shooter, speed=SHOOTER_DEFAULT_SHOT_SPEED):
        self.sidearm = sidearm
        self.shooter = shooter
        self.shootstep = 0
        #
        # use tuples of unchangeable things
        # reset is really just a placeholder in the actions 
        self.shootactions = ((self.reset, "resetting", None),
                             (self.reach, "reaching-out", kForward),
                             (self.shoot, "spinning-up-to-shoot", speed),
                             (self.reach, "pulling-back", kReverse)
                            )

    def reset(self):
        """
        This manipulates the SideShooter to the reset state.
        It also resets the state for the sequence.
        """
        self.reach(kReverse)    # retract arm
        self.shooter.set(0)     # spin down
        self.shootstep = 0
        
    #
    # Actions to shoot (reach, shoot, retract)
    #
    def reach(self, direction):
        self.sidearm.set(direction) 

    def shoot(self, speed):
        self.shooter.set(speed)

    #
    # sequence through active steps (skip over 0)
    #
    def nextAction(self):
        self.shootstep = (self.shootstep % 3) + 1
        
    def doAction(self):
        if (self.shootstep != 0):
            try:
                action = self.shootactions[self.shootstep]
                action[0](action[2])
            except IndexError:
                self.reset()

    def state(self):
        """
        Return a string representing the state of the shooter
        """
        try:
            state_name = self.shootactions[self.shootstep][1]
        except IndexError:
            state_name = "Unknown"
        
    def __str__(self):
        """
        This is a special function that represents the state of the
        SideArmShooter as a string.   If someone tries to print the object
        using:
           sas = SideArmShooter(...)
           print(sas)
        It would print what this function prints.
        s = str(sas) would put the return value of this function into the variable s
        """
        return "SideArmShooter(state={})".format(self.state())


if __name__ == "__main__":
    """
    Run unit test code when someone runs this file directly
    """

    from fakelib import FakeDoubleSolenoid, FakeMotorController

    speed = 0.5
    ds = FakeDoubleSolenoid("forword", "reverse")
    mc = FakeMotorController("can-id")
    sas = SideArmShooter(ds, mc, speed)

    assert(sas.shootstep == 0)
    
    sas.reset()
    assert(sas.shootstep == 0)
    assert(sas.sidearm.state == kReverse)
    assert(sas.shooter.get() == 0)

    sas.nextAction()
    assert(sas.shootstep == 1)
    assert(sas.sidearm.state == kReverse)
    assert(sas.shooter.get() == 0)

    sas.doAction()
    assert(sas.shootstep == 1)
    assert(sas.sidearm.state == kForward)
    assert(sas.shooter.get() == 0)
    
    sas.nextAction()
    sas.doAction()
    assert(sas.shooter.get() == speed)
    
    sas.nextAction()
    assert(sas.shootstep == 3)

    sas.doAction()
    assert(sas.sidearm.state == kReverse)

    sas.nextAction()
    # wrap around to 1 again
    assert(sas.shootstep == 1)

    print("All Tests Pass!")
