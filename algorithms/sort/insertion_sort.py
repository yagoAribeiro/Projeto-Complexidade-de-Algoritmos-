from algorithms.sort.sort_base import PlotableSort


class InsertionSort(PlotableSort):
    def __init__(self):
        super().__init__()

    def iterativeSort(self, data=[]):
        for i in range(1, len(data)):
            chave = data[i]
            j = i - 1
            while j >= 0 and data[j] > chave:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = chave
        return data
    
    def recursiveSort(self, data=[]):
        teste = self.recursiveSort(data)
        return teste

    
    def toString(self): 
        return "Método Insertion Sort"
    

    def recursiveSort(self, data=[]):
        if len(data) <= 1:
            return data
        else:
            key = data[-1]
            data = data[:-1]
            data = self.recursiveSort(data)
            data = self.insert(data, key)
            return data

    def insert(self, data, key):
        if len(data) == 0 or data[-1] <= key:
            data.append(key)
            return data
        else:
            data = data[:-1]
            data = self.insert(data, key)
            data.append(data[-1])
            return data