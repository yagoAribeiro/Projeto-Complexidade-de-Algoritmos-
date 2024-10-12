from algorithms.search.search_base import PlotableSearch

class BuscaLinear(PlotableSearch):
    def __init__(self):
        super().__init__()
    
    def iterativeSearch(self, x, data=[]):
        for i in range(len(data)):
            if (data[i] == x): return i
    
    def recursiveSearch(self, x, data=[]):
        return super().recursiveSearch(x, data)
    
    def toString(self): 
        return "Busca Linear"