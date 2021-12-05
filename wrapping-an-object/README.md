A wrapper class is a kind of software design pattern.
Design patterns are best practice software designs that have been cataloged and named.

The simplest wrapper just wraps one object with another in order to present a different interface --- without changing the class being wrapped.

This is particularly useful for the task of adapting
the Freenove library so that it looks more like the wpilib.

More information about wrapper design patterns can be found
here:

http://public.africa.cmu.edu/cbishop/jsmart/notes/Wrappers.html

This bit of example code shows a class with a particularly ugly interface being wrapped by one with a prettier interface.


Look at the uglylib code, and run the
use_ugly.py program.

            python3 use_ugly.py


Then look at the pretty.py wrapper that improves the
interface.    And run it.

            python3 use_pretty.py

Notice that it fullfills the same function, but
it completely hides the ugly class from the user.
