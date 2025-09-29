import testGenerators
import IterModule

    
x = IterModule.TestIterAndGen()
list = [1, 2, 3]
x.iterateMe(list)
dict = {"key1": 1, "key2": 2}
x.iterateMe(dict)
tup = ("one", "two" , 3)
x.iterateMe(tup)

# Iterate using index by step of 2
x.iterateOverMeAgain(list)

# Comprehension
# Return a new list object based on a condition, without impacting the old list
# newlist = [expression for item in iterable if condition == True]
class TestComp:
    def __init__(self):
        self.fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    def getFruitsWithoutApple(self):
        return [item for item in self.fruits if item != "apple"]

x = TestComp()
newFruits = x.getFruitsWithoutApple()

# Module methods use --
testGenerators.iterateOverMe(newFruits)
# Iterate over dummy list of dictionary
testGenerators.iterateOverPersonList()

#Iterate using a Generator
for person in testGenerators.generatorTemp():
    print("From Gen1: ", person)

# Iterate using a Generator Expression
for person in testGenerators.generatorTemp2():
    print("From Gen2: ",person)