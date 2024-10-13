from algorithms.sort.sort_base import PlotableSort

class MergeSort(PlotableSort):
    def __init__(self):
        super().__init__()

    def iterativeSort(self, data=[]):
        data2 = self.merge_sort_iterativo(data)
        return data2
    
    def recursiveSort(self, data=[]):
        teste = self.merge_sort_recursivo(data)
        return teste
    
    def toString(self): 
        return "Método Merge Sort"

    def merge_sort_iterativo(self, data):
        width = 1
        n = len(data)
        temp = [0] * n

        while width < n:
            for i in range(0, n, 2 * width):
                left = i
                mid = min(i + width, n)
                right = min(i + 2 * width, n)
                self.merge(data, temp, left, mid, right)
            data[:] = temp[:]
            width *= 2

    def merge(self, data, temp, left, mid, right):
        i, j, k = left, mid, left
        while i < mid and j < right:
            if data[i] <= data[j]:
                temp[k] = data[i]
                i += 1
            else:
                temp[k] = data[j]
                j += 1
            k += 1
        while i < mid:
            temp[k] = data[i]
            i += 1
            k += 1
        while j < right:
            temp[k] = data[j]
            j += 1
            k += 1


    def merge_sort_recursivo(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.merge_sort_recursivo(data[:mid])
        right = self.merge_sort_recursivo(data[mid:])
        return self.merge2(left, right)

    def merge2(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result