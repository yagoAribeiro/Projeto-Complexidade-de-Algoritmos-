from algorithms.search.search_base import PlotableSearch

class BuscaBinaria(PlotableSearch):
    def __init__(self):
        super().__init__()
    
    def iterativeSearch(self, x, data=[]):
        left = 0
        right = len(data)-1
        while(left<=right):
            middle = (left+right)/2
            if middle==x: return middle
            elif x < middle:
                right = middle-1
            else:
                left = middle+1

    
    def recursiveSearch(self, x, data=[]):
        return self.recursionSearch(x, data, 0, len(data)-1)
    
    def recursionSearch(self, x, data, left, right):
        if left<=right: return -1
        middle = (left+right)/2
        if middle==x: return middle
        elif x < middle:
            return self.recursionSearch(x, data, left, middle-1)
        else:
            return self.recursionSearch(x, data, middle+1, right)
    
    def toString(self):
        return "Busca Binária"