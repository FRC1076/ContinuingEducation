A wrapper class is a kind of software design pattern.
Design patterns are best practices in software that have been cataloged and named.

The simplest wrapper is called an Adapter. It wraps a class (the Adaptee) in order to present a different interface --- without changing the class being wrapped.

This is particularly useful for the task of adapting
the Freenove library so that it looks more like wpilib (pikitlib)

More information about other wrapper design patterns can be found
here:

http://public.africa.cmu.edu/cbishop/jsmart/notes/Wrappers.html

This bit of example code shows a class with a particularly ugly interface being wrapped by an Adapter with a prettier interface.

This problem illustrates Adapting an unpleasant interface in the uglylib
so it is no longer ugly.


Look at the uglylib/ugly code, and run the
use_ugly.py program.

            python3 use_ugly.py


Then look at the pretty.py wrapper that translates(adapts) the
interface.    And run it.

            python3 use_pretty.py

Notice that it has the same function, but
it completely hides the ugly class from the user.

We want to Adapt most of the Freenove library elements
using classes that are part of the wpilib library.
That was, the Freenove can serve as a platform to learn
how to program the competition robot.


