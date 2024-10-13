from algorithms.sort.sort_base import PlotableSort

class BubbleSort(PlotableSort):
    def __init__(self):
        super().__init__()
        
    # Implementação do Bubble Sort Iterativo
    def iterativeSort(self, data=[]):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data
    
    # Implementação do Bubble Sort Recursivo
    def recursiveSort(self, data=[]):
        n = len(data)
        if n <= 1:
            return data
        for i in range(n-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
        return self.recursiveSort(data[:-1]) + [data[-1]]
    
    def toString(self):
        return "Método Bubble Sort"