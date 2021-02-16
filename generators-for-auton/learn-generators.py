#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
#
#   When you call a function that contains the "yield"
#   comand in it, the function returns a generator.
#
def yesman0():
    print("yes 1")
    yield
    print("yes 2")
    yield
    print("I really mean yes")

# calling the function yields a generator, but nothing else
# Notice, no printing occurs when the generator gets created
ygen = yesman0()
print("This is a generator object: {}".format(ygen))


# In[ ]:


# generator object handles next() and runs until it encounters the next yield keyword
next(ygen)    #  prints yes1 and then returns at first yield
next(ygen)    #  continues from there, printing yes2 and returning at second yield
next(ygen)    #  continues from there, printing final message and then throwing StopIteration exception


# In[ ]:


# notice the third call does the print, but then throws the
# StopIteration exception.     Typical iteration constructs will catch that
# and handle it gracefully.
#
# Since we are using explicit next() call to do iteration, you will your
# own thing, you'll need to catch it.
# Below we catch the end of the iteration and break out of the loop

ygen = yesman0()
while True:
    try:
        next(ygen)
        time.sleep(1.0)
    except StopIteration:
        break


# In[ ]:


# By catching the StopIteration exception and using it to determine
# to break out of the infinite loop, we end up with a graceful exit.       

# Also ordinary (for _ in) iteration works fine, since it stops when the
# StopIteration occurs.     This is a pretty compact.
for _ in yesman0():
    time.sleep(1.0)


# In[ ]:


# You can wrap up a generator in another function and make it
# a generator.  This generator lets you compose two generators
# back to back.   When one finishes, the other continues.
def yesmen0():
    yield from yesman0()
    yield from yesman0()

for _ in yesmen0():
    time.sleep(0.5)


# In[ ]:


# generators can generate forever
def always_yes():
    while True:
        print("yes")
        yield

#  type ctrl-c to stop this if you are running
#  it in a command shell, use the square "stop" button
#  if you are running in jupyter notebook
for _ in always_yes():
    time.sleep(1.0)


# In[ ]:


#  generators can return things that the caller can use
#  Return values using the "yield" command, e.g. yield <return-value>
def infinite_yeses():
    while True:
        yield "yes"

# notice that the generator now looks like an infinite collection
# of answers  (ctrl-c or stop button will stop this)
for answer in infinite_yeses():
    print(answer)
    time.sleep(1)


# In[ ]:


# of course, you can make the generator more useful by
# being able to change its behavior depending on how you create it.
def answerman(answer):
    while True:
        yield answer

for answer in answerman("no"):
    print(answer)
    time.sleep(1)


# In[ ]:


def oncewaffle(choices):
    for choice in choices:
        yield choice

# will generate the collection of answers once (not so interesting)
for answer in oncewaffle(["yes", "no", "maybe", "later"]):
    print(answer)
    time.sleep(1)


# In[ ]:


# more interesting, perhaps is a generator that never tires of answering
def foreverwaffle(choices):
    while True:
        for choice in choices:
            yield choice

# will generate an infinite number of choices (in rotation)
# ctrl-c or stop button will stop this
for answer in foreverwaffle(["yes", "no", "maybe", "later"]):
    print(answer)
    time.sleep(1)


# In[ ]:


# Sometimes we would rather that our generator optionally stop generating.
# Sometimes, you may want to limit how much time a generator works.   Or
# maybe stop if some condition occurs.  Let's say that you just want it
# to generate for 3 seconds.

def momentary_answerman(answer, duration):
    stop_time = time.time() + duration
    while time.time() <= stop_time:
        yield answer

for answer in momentary_answerman("maybe", 3):
    print(answer)
    time.sleep(0.25)


# In[ ]:


# As we get a bit closer to doing robotics applications, we'll need parts
# of robots to do testing.     These are stubs that stand-in for real robot
# functions, but just print messages, so we know what is happening.


class FakeDriveTrain:
    """
    Fake drivetrain is just a stand-in for a real drivetrain.
    Used for this demonstration.   It just prints out what it is doing.
    Give it a name when you make it, and it includes the name
    in the output message.
    """
    def __init__(self, train):
        self.train = train
    
    def driveArcade(self, forward, rotate):
        if forward == 0 and rotate == 0:
            print("{} is STOPPED".format(self.train))
        else:
            print("Driving {} forward {} and rotating {}".format(self.train, forward, rotate))

#
#  So, now you have a framework for doing a task with given arguments
#  (so far, only printing a string, but we can make it more sophisticated)
#  Once time expires, the loop ends, and the drivetrain is stopped.   (usually a good thing)
#
def timed_arcadedrive(duration, drivetrain, forward, rotate):
    stop_time = time.time() + duration
    while time.time() <= stop_time:
        drivetrain.driveArcade(forward, rotate)
        yield
    drivetrain.driveArcade(0, 0)

dt = FakeDriveTrain("arcade")
drive_auton = timed_arcadedrive(5, dt, 1.0, 0)

for _ in drive_auton:
    time.sleep(1.0)

    


# In[ ]:


#
#  But, then we have to have a timed_xxx() function for every kind of thing.
#  Perhaps it would be better to define a generic AutoTask object that has
#  a do_step() method.   Then, as long as any subtask is an AutoTask object,
#  or at least has a do_step() method, we can ask the timed_xxxx() function to
#  call the do_step() until the time expires.
#
class AutoTask:
    """
    Nobody should create an AutoTask object.  This is just
    a template for what derived classes should implement.
    """
    def __init__(self):
        pass

    def do_step(self):
        pass
    

class AutoArcade(AutoTask):
    def __init__(self, train, forward, rotate):
        """
        The task has to store all of the state necessary for
        the do_step method to be callable with no arguments.
        This way, the timed_xxx() function knows *nothing*
        about the subtask.
        """
        self.train = train
        self.forward = forward
        self.rotate = rotate

    def do_step(self):
        """
        Here is the meat of the generic-looking step.   It
        puts all of the saved state together to do the thing.
        """
        self.train.driveArcade(self.forward, self.rotate)

#
#  Now timed_task() looks more generic.   You can hand it any task
#  and it can step the task for the specified amount of time.
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
# auton steps the drive_task for 7 seconds
auton = timed_task(7, drive_task)

for _ in auton:
    time.sleep(1.0)


# In[ ]:


# We can assemble things compactly (with labels) so that
# the plan is more clear and fits on a single line

for _ in timed_task(duration=7, task=AutoArcade(train=dt, forward=1.0, rotate=0.1)):
    time.sleep(3.5)


# In[ ]:


# if we use the "yield from" operator, we can compose several
# autonomous plans together.     But to get a generator out
# of it, we have to put it into a function and call the function.

def full_auton(train):
    """
    Chain two autonomous plans together into a single generator
    """
    yield from timed_task(5.0, AutoArcade(train, 1.0, 0.0))
    yield from timed_task(4.0, AutoArcade(train, -1.0, 0.0))

for _ in full_auton(dt):
    time.sleep(1.0)


# In[ ]:


# sometimes we don't want to run the AutoTask for the full length of time.
# For example, we might want to drive until we are within 5cm of the target

# For this we need an UltraSonic sensor (why am I not surprised?)
class FakeUltraSonic:
    """
    Since this is not a real sonar unit, we can load the range readings into it
    as an iterator that produces the target ranges
    """
    def __init__(self, range_iter):
        self.range_iter = range_iter
    
    def range_cm(self):
        """
        Ultrasonic just returns successive elements of
        the iterator that was passed to the constructor.
        When that runs out, it just returns 0. (slam!)
        """
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
        if self.sonar.range_cm() <= self.end_range_cm:
            print("Within range: {}".format(self.end_range_cm))
            self.train.driveArcade(0, 0)
            return False
        else:
            self.train.driveArcade(self.forward, self.rotate)
            return True


#  We have to upgrade the timed_task wrapper so it can interpret the return
#  value from do_step(). We keep going as long as do_step() returns true.
#  Once it returns false, we break out of the loop (and the generator ends)
def timed_task(duration, task):
    stop_time = time.time() + duration
    while time.time() <= stop_time:
        if task.do_step():
            yield
        else:
            break

#
# 
# readings will be 9, 8, 7, 6, 5, 4, .... 0, 0, 0  ouch, ouch, ouch
#
us = FakeUltraSonic(iter(range(9, 0, -1)))
dt = FakeDriveTrain("FAKE-FOR-US-AUTON")

# drive until within 5cm of the target or at most for
# AutoDriveToTarget needs a drivetrain and an ultrasonic
drivetask = AutoDriveToTarget(dt, 0.5, 0, us, 5.0)

# do drivetask no longer than 7 seconds
print("Drive no longer than 7 seconds")
for _ in timed_task(7, drivetask):
    time.sleep(1.0)


# In[ ]:


#
# 
# readings will be 9, 8, 7, 6, 5, 4, .... 0
#
us = FakeUltraSonic(iter(range(9, 0, -1)))
dt = FakeDriveTrain("FAKE-FOR-US-AUTON")

# drive until within 5cm of the target or at most for
# AutoDriveToTarget needs a drivetrain and an ultrasonic
drivetask = AutoDriveToTarget(dt, 0.5, 0, us, 5.0)

print("Try again, but drive no longer than 3 seconds")
for _ in timed_task(3, drivetask):
    time.sleep(1.0)


# In[ ]:


#  But it is a bit awkward having the subtask require some kind of special
#  return value.   What if the subtask was also a generator?   Then the
#  timed_task wrapper could just "yield from task.do_step()" and the subtask
#  could finish generating when it is done.    Then the rule for building
#  auton tasks is that they are generators, and they stop generating when
#  they reach their objective.   The timed_task wrapper can stop them when
#  their alloted time expires. (in the event they don't reach their objective)
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
    Define the function that will create the generator.
    Return the generator to be the "body" of the task.
    This way, everything does an initialize(), the generator,
    and then the finish().
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


# In[ ]:




