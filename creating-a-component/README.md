
        Adding a component (or two) to pikitlib


This repository contains example code that illustrates the
process that you might use to add a component to the pikitlib.
It uses a fictitious FluxMeter device to act as an example.
Using a fictitious devices is a perfectly legitimate method,
because, it embodies two important concepts:

1.  All devices unknown to you might as well be fictitious,
because you know nothing about them, but, interestingly,

2.  you can still create a software interface to a device that you
do not understand fully when the creator of the device has abstracted
the details in a software interface that you can use (or wrap)
in your implementation.

I'm not saying you should give up on trying to understand these
things, only that you cannot wait until you understand everything
before you do anything, lest you ultimately do nothing.

The first in creating a software component is often to decide on what its interface will be.   In our case, we need
to focus on how to create the component, and how to manipulate the
device controlled by the component.

You can create the interface of your component with no implementation,
(this is called a stub), and even test it out to see how it looks
and works in the robot.py universe.
You can ask others to give you feedback on the interface, and, hopefully
settle on a name that fits in and is properly descriptive.

While making this repository, I changed several names as I worked.
Always be thinking about using the right/best names.

Naming things carefully is actually important, and one of the two most
difficult things in computer science.  The other is cache-coherency and
off-by-one errors.

Here are the files for your enjoyment and enlightenment.   You can
work through thiem in this order, and things should mostly make sense.

* FluxMeter_stub.py  --   write a stub for a component and even test it
* Adc.py             --   Freenove (a.k.a Acme) annotated code for reading data from
                          an Analog to Digital Converter chip
* diagrams.pdf       --   the hardware view of the Freenove FluxMeter solution
* FluxMeter_wrap.py  --   add implementation that uses lower layers
* diagrams.pdf       --   the software view of the Freenove FluxMeter solution
* FluxMeter_on_RIO_stub.py  -- write a stub for a FluxMeter used by RoboRio
* diagrams.pdf       --   the hardware view of the RIO FluxMeter solution
* FluxMeter_on_RIO_wrap.py -- write the implementation using wpilib fake
* diagrams.pdf       --   the software view of the RIO FluxMeter solution
* FluxMeter_improved.py  -- the final version of Freenove solution that reflects the
                            structure preferred for FRC code on the RIO
