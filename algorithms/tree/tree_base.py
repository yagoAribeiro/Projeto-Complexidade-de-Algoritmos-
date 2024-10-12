class PlotableTree:
    def __init__(self):
        pass
    
    def iterativeInsert(self, x):
        raise NotImplementedError("Método de inserção iterativa da árvore não foi implementado!")
    
    def recursiveInsert(self, x):
        raise NotImplementedError("Método de inserção recursiva da árvore não foi implementado!")

    def iterativeSearch(self, x):
        raise NotImplementedError("Método de busca iterativa da árvore não foi implementado!")
    
    def recursiveSearch(self, x):
        raise NotImplementedError("Método de busca recursiva da árvore não foi implementado!")
    
    def iterativeDelete(self, x):
        raise NotImplementedError("Método de remoção iterativa da árvore não foi implementado!")
    
    def recursiveDelete(self, x):
        raise NotImplementedError("Método de remoção recursiva da árvore não foi implementado!")
    
    def toString(self): raise NotImplemented("Método toString não implementado!")