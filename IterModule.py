
class TestIterAndGen:
    def __init__(self):
        print("I am a class for iterating iterables")

    def iterateMe(self, itrObj):
        for i in itrObj:
            print("Value: ", i)

    def iterateOverMeAgain(self, iterable):
        for i in range(0, len(iterable), 2):
            print("Value at", i, " is:", iterable[i])