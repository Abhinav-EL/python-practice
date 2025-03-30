def iterateMeOutside(itrObj):
        for i in itrObj:
            print("Value: ", i)

class TestIterAndGen:
    def __init__(self):
        print("I am a class called TestDataTypes")

    def iterateMe(self, itrObj):
        for i in itrObj:
            print("Value: ", i)
    
x = TestIterAndGen()
list = [1, 2, 3]
x.iterateMe(list)
dict = {"key1": 1, "key2": 2}
x.iterateMe(dict)
tup = ("one", "two" , 3)
x.iterateMe(tup)

# Comprehension
# Return a new list object based on a condition, without impacting the old list
# newlist = [expression for item in iterable if condition == True]
class TestComp:
    def __init__(self):
        self.fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    def getFruitsWithoutApple(self):
        return ["a"+item for item in self.fruits if item != "apple"]

x = TestComp()
newFruits = x.getFruitsWithoutApple()
iterateMeOutside(newFruits)