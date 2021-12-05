
from uglylib.ugly import ReallyTrulyUglyThing

class Pretty:
    """
    Nobody wants to use the Ugly class directly.
    Pretty wraps it to make it look more conventional.

    Usage:
         t = Pretty()
         t.prettyOperation()
    """
    def __init__(self):
        self.ug = ReallyTrulyUglyThing()

    def prettyOperation(self):
        self.ug.someOtherReallyUglyOperation()
