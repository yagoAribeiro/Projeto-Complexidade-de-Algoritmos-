from algorithms.sort.sort_base import PlotableSort

class SelectionSort(PlotableSort):
    def __init__(self):
        super().__init__()

    # Implementação da Selection Sort Iterativo
    def iterativeSort(self, data=[]):
        n = len(data)
        for i in range(n):
            menor_idx = i
            for j in range(i + 1, n):
                if data[j] < data[menor_idx]:
                    menor_idx = j
        
            data[i], data[menor_idx] = data[menor_idx], data[i]

    # Implementação da Selection Sort Recursivo
    def recursiveSort(self, data=[], index=0):
        if index >= len(data) - 1:
            return
        min_index = index
        for i in range(index + 1, len(data)):
            if data[i] < data[min_index]:
                min_index = i
        data[index], data[min_index] = data[min_index], data[index]
        self.recursiveSort(data, index + 1)

    def toString(self): 
        return "Método Selection Sort"
