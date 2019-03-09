import unittest

from person import Person
 
class PersonTest(unittest.TestCase):
    def test_east_tx_hello(self):
        p1 = Person('Earl', '1963-11-04', "Texas", "Heidi, y'all")
        self.assertEqual(p1.hello(),"Heidi, y'all. I'm from Texas.")

    def test_maine_hello(self):
        p1 = Person('Sarah', '1980-09-02', "Maine", "HeyHowAhYa")
        self.assertEqual(p1.hello(),"HeyHowAhYa. I'm from Maine.")

if __name__ == '__main__':
    unittest.main()

