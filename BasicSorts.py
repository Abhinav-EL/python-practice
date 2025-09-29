import IterModule
from SortInterface import SortInterface

# One of the elementary sorts. 
# Loop through, find the min and replace with the current pointer.
# Has to keep track using the pointer and not the actual value because values need to be swapped.
class SelectionSort(SortInterface):
    def sort_me(self, toSortList):
        for i in range(0, len(toSortList)):
            min = i
            for j in range(i+1, len(toSortList)):
                if(toSortList[j]<toSortList[min]):
                    min = j
            if(min!=i):
                self.swap(toSortList, i, min)

# One of the elementary sorts. 
# Traverse in reverse order, find the smallest value and then replace.
class InsertionSort(SortInterface):
    def sort_me(self, toSortList):
        for i in range(0, len(toSortList)):
            for j in range(i, 0, -1):
                if(toSortList[j]< toSortList[j-1]):
                    self.swap(toSortList, j, j-1)

tester = IterModule.TestIterAndGen()
toSortList = [5, 4, 0, 10, 3]
#tester.iterateMe(toSortList)

#selectionSort = SelectionSort()
#selectionSort.sort_me(toSortList=toSortList)

insertionSort = InsertionSort()
insertionSort.sort_me(toSortList=toSortList)

tester.iterateMe(toSortList)