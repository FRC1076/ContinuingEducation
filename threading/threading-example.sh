5i3RRA-Book:ContinuingEducation matthewj$ python3
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from threading import Thread
>>> from time import sleep
>>> def do_this_for_n_that_for_m_and_then_something(n, m):
...     print("Started doing THIS for {} seconds".format(n))
...     sleep(n)
...     print("Now doing THAT for {} seconds".format(m))
...     sleep(m)
...     print("Now doing SOMETHING")
... 
>>># robot loop does something essential every second
... for loopCount in range(20):
...     if loopCount == 3:
...         thr = Thread(target=do_this_for_n_that_for_m_and_then_something, args=(5, 7))
...         thr.start()
...     print("Doing the essential in second {}".format(loopCount))
...     sleep(1)
... 
Doing the essential in second 0
Doing the essential in second 1
Doing the essential in second 2
Started doing THIS for 5 seconds
Doing the essential in second 3
Doing the essential in second 4
Doing the essential in second 5
Doing the essential in second 6
Doing the essential in second 7
Now doing THAT for 7 seconds
Doing the essential in second 8
Doing the essential in second 9
Doing the essential in second 10
Doing the essential in second 11
Doing the essential in second 12
Doing the essential in second 13
Doing the essential in second 14
Now doing SOMETHING
Doing the essential in second 15
Doing the essential in second 16
Doing the essential in second 17
Doing the essential in second 18
Doing the essential in second 19




# if you want to try this, just open up a python shell and
# paste this in.
from threading import Thread
from time import sleep
def do_this_for_n_that_for_m_and_then_something(n, m):
    print("Started doing THIS for {} seconds".format(n))
    sleep(n)
    print("Now doing THAT for {} seconds".format(m))
    sleep(m)
    print("Now doing SOMETHING")

# robot loop does something essential every second
for loopCount in range(20):
    if loopCount == 3:
        thr = Thread(target=do_this_for_n_that_for_m_and_then_something, args=(5, 7))
        thr.start()
    print("Doing the essential in second {}".format(loopCount))
    sleep(1)
