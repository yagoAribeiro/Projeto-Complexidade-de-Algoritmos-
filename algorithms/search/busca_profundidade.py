from algorithms.search.search_base import PlotableSearch

class BuscaProfundidade(PlotableSearch):
    def __init__(self):
        super().__init__()
    
    def iterativeSearch(self, x, data=[]):
        visitados = []
        for i in range(len(data)):
            if x == i: return i
            visitados.append(i)
            for vizinho in data[i]:
                if vizinho not in visitados:
                    if x == vizinho: return vizinho
                    visitados.append(vizinho)

    
    def recursiveSearch(self, x, data=[], visitados=[], i = 0):
        return self.recursionSearch(x, data, [], i, len(data))
    
    def recursionSearch(self, x, data=[], visitados=[], i = 0, limit = 0):
        if i >= limit: return -1
        if i not in visitados:
            if i == x: return i
            visitados.append(i)
            self.recursionSearch(data[i], visitados, i+1, limit)
        return -1


    def toString(self): 
        return "Busca por Profundidade"