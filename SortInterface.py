import abc

class SortInterface(abc.ABC):
    @abc.abstractmethod
    def sort_me(self):
        pass

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp