import testmodule

class TestIterAndGen:
    def __init__(self):
        print("I am a class called TestDataTypes")

    def iterateMe(self, itrObj):
        for i in itrObj:
            print("Value: ", i)

    def iterateOverMeAgain(self, iterable):
        for i in range(0, len(iterable), 2):
            print("Value at", i, " is:", iterable[i])

    
x = TestIterAndGen()
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
testmodule.iterateOverMe(newFruits)
# Iterate over dummy list of dictionary
testmodule.iterateOverPersonList()

#Iterate using a Generator
for person in testmodule.generatorTemp():
    print("From Gen1: ", person)

# Iterate using a Generator Expression
for person in testmodule.generatorTemp2():
    print("From Gen2: ",person)