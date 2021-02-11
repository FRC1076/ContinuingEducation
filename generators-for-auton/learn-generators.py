import time
#
#   When you call a function that contains the "yield"
#   comand in it, the function returns a generator.
#
def yesman():
    print("yes 1")
    yield
    print("yes 2")
    yield
    print("I really mean yes")

# calling the function yields a generator, but nothing else
# Notice, no printing occurs when the generator gets created
ygen = yesman()

# generator object handles next() and runs until the next yield keyword
next(ygen)    #  prints yes1 and then returns at first yield
next(ygen)    #  continues from there, printing yes2 and returning at second yield
next(ygen)    #  continues from there, printing final message and then throwing StopIteration

# notice the third call does the print, but then throws the
# StopIteration exception.     Typical iteration catches that.
# If you are doing your own thing, you'll need to catch it.
# Below we catch the end of the iteration and break out of the loop

ygen = yesman()
while True:
    try:
        next(ygen)
        time.sleep(1.0)
    except StopIteration:
        break

# But just regular iteration works fine, since it stops when the
# StopIteration occurs.     This is pretty compact.
for _ in yesman():
    time.sleep(1.0)


# You can wrap up a generator in another function and make it
# a generator.  This generator lets you compose two generators
# back to back.   When one finishes, the other starts.
def yesmen():
    yield from yesman()
    yield from yesman()

for _ in yesmen():
    time.sleep(0.5)


# generators can generate forever
def yesman():
    while True:
        print("yes")
        yield

#  type ctrl-c to stop this
for _ in yesman():
    time.sleep(1)


#  generators can return things that the caller can use
#  Return values using yield command, yield <return-value>
def foreveryes():
    while True:
        yield "yes"

# notice now that the generator looks like an infinite collection
# of answers
for answer in foreveryes():
    print(answer)
    time.sleep(1)


# of course, you can make the generator more useful by
# being able to change its behavior depending on how you create it.
def answerman(answer):
    while True:
        yield answer

for answer in answerman("no"):
    print(answer)
    time.sleep(1)

def foreverwaffle(choices):
    while True:
        for choice in choices:
            yield choice

# can generate an infinite number of choices (in rotation)
for answer in foreverwaffle(["yes", "no", "maybe", "later"]):
    print(answer)
    time.sleep(1)


# Infinite collections are not always interesting.  Sometimes, you
# want to limit how much time a generator works.   Let's say that you
# just want it to generate for 5 seconds.

def momentary_answerman(answer, duration):
    stop_time = time.time() + duration
    while time.time() <= stop_time:
        yield answer

for answer in momentary_answerman("maybe", 5):
    print(answer)
    time.sleep(1)

class FakeDriveTrain:
    """
    Fake drivetrain is just a stand-in for a real drivetrain.
    Used for demonstration.   It just prints out what it is doing.
    Give it a name when you make it, and it includes the name
    in the output message.
    """
    def __init__(self, train):
        self.train = train
    
    def driveArcade(self, forward, rotate):
        print("Driving {} forward {} and rotating {}".format(self.train, forward, rotate))

#
#  So, now you have a framework for doing a task with given arguments
#  (so far, only printing a string, but we can make it more sophisticated)
#
def timed_arcadedrive(duration, drivetrain, forward, rotate):
    stop_time = time.time() + duration
    while time.time() <= stop_time:
        drivetrain.driveArcade(forward, rotate)
        yield

dt = FakeDriveTrain("arcade")
drive_auton = timed_arcadedrive(5, dt, 1.0, 0)

for _ in drive_auton:
    time.sleep(1)

#
#  But, then we have to have a momentary function for every kind of thing.
#  Perhaps it would be better to define a generic AutoTask object that has
#  a do_step() method.   Then, as long as any subtask is an AutoTask object,
#  or at least has a do_step() method, we can ask the timed_xxxx() function to
#  call the do_step() until the time expires.
#

class AutoTask:
    def __init__(self):
        pass

    def do_step(self):
        pass

class AutoArcade(AutoTask):
    def __init__(self, train, forward, rotate):
        """
        The task has to store all of the state necessary for
        the time method to be callable with no arguments.
        This way, the timed_xxx() function knows *nothing*
        about the subtask.
        """
        self.train = train
        self.forward = forward
        self.rotate = rotate

    def do_step(self):
        self.train.driveArcade(self.forward, self.rotate)

#
#  Now this looks more generic.   You can hand it any task
#  it can step the task for the specified amount of time.
#
def timed_task(duration, task):
    stop_time = time.time() + duration
    while time.time() <= stop_time:
        task.do_step()
        yield

# create the drivetrain
dt = FakeDriveTrain("Arcade")
# create the driving subtask
drive_task = AutoArcade(dt, 1.0, 0.1)

# auton drives the task for  seconds
auton = timed_task(7, drive_task)

for _ in auton:
    time.sleep(1.0)


# We can assemble things a little differently so that
# the plan is more readable

auton = timed_task(5.0, AutoArcade(dt, 1.0, 0.1))
for _ in auton:
    time.sleep(1.0)

# if use the "yield from" operator, we can compose several
# automous plans together.     But to get a generator out
# of it, we have to put it into a function and call the function.

def full_auton(train):
    """
    Chain two autonomous plans together into a single generator
    """
    yield from timed_task(5.0, AutoArcade(train, 1.0, 0.0))
    yield from timed_task(4.0, AutoArcade(train, -1.0, 0.0))


for _ in full_auton(dt):
    time.sleep(1.0)


# sometimes we don't want to run the AutoTask for the full length of time.
# For example, we might want to drive until we are within 5cm of the target

# For this we need an UltraSonic sensor
class FakeUltraSonic:
    """
    Since this is not a real sonar unit, we can load the range readings into it
    as an iterator that produces the target ranges
    """
    def __init__(self, range_iter):
        self.range_iter = range_iter
    
    def range_cm(self):
        try:
            cm = next(self.range_iter)
            print("range to target: {}cm".format(cm))
        except StopIteration:
            cm = 0
        return cm

class AutoDriveToTarget(AutoTask):
    """
    Need more arguments to create the more complex auto plan
    """
    def __init__(self, train, forward, rotate, sonar, end_range_cm):
        """
        The task has to store all of the state necessary for
        the time method to be callable with no arguments.
        """
        self.train = train
        self.forward = forward
        self.rotate = rotate
        self.sonar = sonar
        self.end_range_cm = end_range_cm
    
    def do_step(self):
        """
        Now we can't just do our thing, we have to tell the caller
        whether or not we are done driving.   So, we can return a
        True if we keep going, or False if we are done
        """
        if self.sonar.range_cm() < self.end_range_cm:
            self.train.driveArcade(0, 0)
            return False
        else:
            self.train.driveArcade(self.forward, self.rotate)
            return True


#  But we have to upgrade the timed_task wrapper so it can interpret the return
#  value from do_step()
def timed_task(duration, task):
    stop_time = time.time() + duration
    while time.time() <= stop_time:
        if task.do_step():
            yield
        else:
            break


#
# drive until within 5cm of the target or at most for
# readings will be 9, 8, 7, 6, 5, 4, .... 0
#
us = FakeUltraSonic(iter(range(9, 0, -1)))
dt = FakeDriveTrain("FAKE")

# AutoDriveToTarget needs a drivetrain and an ultrasonic
drivetask = AutoDriveToTarget(dt, 0.5, 0, us, 5.0)
# do drivetask no longer than 5 seconds
for _ in timed_task(5, drivetask):
    time.sleep(0.5)



#  But it is a bit awkward having the subtask require some kind of special
#  return value.   What if the subtask was also a generator?   Then the
#  timed_task wrapper could just "yield from task.do_step()" and the subtask
#  could finish generating when it is done.    Then the rule for building
#  auton tasks is that they are generators, and they stop generating when
#  the reach their objective.   The timed_task wrapper can stop them when
#  their alloted time expires.
#
#  This can really simplify the writing of autonomous tasks, but it does
#  mean the infrastructure has to be a bit more sophisticated.    This is
#  because we need to evaluate a function in the subtask that contains a
#  "yield" in order to get a generator that the parent (timed) task can
#  yield from.
#
#  Generally, when we define an autonomous task, it takes a certain form.
#  It needs some initialization (to grab the current time, or, to reset
#  something), it needs the actual steps, and it may need some kind of
#  stop action.    If you could create a generator framework that would
#  support that, you could use it to make a rich variety of tasks.
#
#  But, remember the function that creates the generator doesn't do anything
#  when the generator is first created, so we miss out on an initialization
#  opportunity unless the generator is always created immediately after
#  an initialization task is done.   That may not be convenient.
#  So we add another level where we define the function generator and call/return
#  it from the run() call:
#
def initialize():
    print("initialize")

def finish():
    print("finish")

def ideal_auton_run():
    """
    Define the function that will create the generator
    """
    def the_generator():
        for i in range(10):
            print("step {}".format(i))
            yield
        finish()
    
    initialize()
    return the_generator()


auton = ideal_auton_run()
for _ in auton:
    time.sleep(1.0)

