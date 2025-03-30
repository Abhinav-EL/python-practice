# Mutable objects can have surprising effects at the class level.
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Dean')
d.add_trick('Rollover')
e = Dog('Jim')
e.add_trick('Raise Paw')
print("Dog tricks: ", e.tricks) # print both tricks


class DogV2:

    def __init__(self, name):
        self.name = name
        self.tricks = [] # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

f = DogV2('Abe')
f.add_trick('Rollover')
g = DogV2('Cane')
g.add_trick('Another Trick')
print("Dog tricks: ", g.tricks)