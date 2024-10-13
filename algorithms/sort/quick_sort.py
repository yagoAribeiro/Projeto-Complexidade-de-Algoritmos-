
from algorithms.sort.sort_base import PlotableSort

class QuickSort(PlotableSort):
    def __init__(self):
        super().__init__()

    def iterativeSort(self, data=[]):
        data = self.quick_sort_iterative(data)
        return data
    
    def recursiveSort(self, data=[]):
        data = self.quick_sort_recursive(data, 0, len(data) - 1)
        return data
    
    def toString(self):
        return "Método Quick Sort"
    
    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort_recursive(arr, low, pi - 1)
            self.quick_sort_recursive(arr, pi + 1, high)
        return arr

    def quick_sort_iterative(self, arr):
        size = len(arr)
        stack = []
        stack.append(0)
        stack.append(size - 1)

        while stack:
            high = stack.pop()
            low = stack.pop()

            pi = self.partition(arr, low, high)

            if pi - 1 > low:
                stack.append(low)
                stack.append(pi - 1)

            if pi + 1 < high:
                stack.append(pi + 1)
                stack.append(high)

        return arr