from algorithms.search.search_base import PlotableSearch

class BuscaLinear(PlotableSearch):
    def __init__(self):
        super().__init__()
        
    # Implementação da Busca Linear Iterativa
    def iterativeSearch(self, x, data=[]):
        for i in range(len(data)):
            if data[i] == x:
                return i
        return -1
    
    # Implementação da Busca Linear Recursiva
    def recursiveSearch(self, x, data=[], i=0):
        if i >= len(data):
            return -1
        if data[i] == x:
            return i
        return self.recursiveSearch(x, data, i + 1)
    
    def toString(self):
        return "Busca Linear"