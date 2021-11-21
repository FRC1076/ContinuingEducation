class Person:
    def __init__(self, name, where_from, dob, greeting):
        self.name = name
        self.where_from = where_from
        self.dob = dob
        self.greeting = greeting

    def hello(self):
        pass

    def age(self):
        """
        See if you can find a python library to help with date math
        """
        pass

#  Handy Person is composition of a person and a skill
class HandyPerson:

    def __init__(self, name, where_from, dob, greeting, skill):
        self.person = Person(name, where_from, dob, greeting)
        self.skill = skill
    
    def hello(self):
        pass

    def age(self):
        pass
    
    def repair(self):
        pass
    
