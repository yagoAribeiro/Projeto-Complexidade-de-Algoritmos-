from algorithms.search.search_base import PlotableSearch

class BuscaBinaria(PlotableSearch):
    def __init__(self):
        super().__init__()

    # Implementação da Busca Binaria Iterativa
    def iterativeSearch(self, x, data=[]):
    inicio = 0
    fim = len(arr) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if arr[meio] == elemento:
            return meio
        
        elif elemento < arr[meio]:
            fim = meio - 1
        
        else:
            inicio = meio + 1
            
    return -1

    # Implementação da Busca Binaria Recursiva
    def recursiveSearch(self, x, data=[]):
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2    
    
    if arr[meio] == elemento:
        return meio
    
    elif elemento < arr[meio]:
        return busca_binaria(arr, elemento, inicio, meio - 1)
    
    else:
        return busca_binaria(arr, elemento, meio + 1, fim)
    
    def toString(self):
        return "Busca Binária"
