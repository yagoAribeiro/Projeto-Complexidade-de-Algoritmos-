from algorithms.sort.sort_base import PlotableSort

class SelectionSort(PlotableSort):
    def __init__(self):
        super().__init__()

    # Implementação da Selection Sort Iterativo
    def iterativeSort(self, data=[]):
    n = len(arr)
    
    for i in range(n):
        menor_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[menor_idx]:
                menor_idx = j
        
        arr[i], arr[menor_idx] = arr[menor_idx], arr[i]

    # Implementação da Selection Sort Recursivo
    def recursiveSort(self, data=[]):
    if i >= n - 1:
        return
    
    menor_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[menor_idx]:
            menor_idx = j

    arr[i], arr[menor_idx] = arr[menor_idx], arr[i]
    
    selection_sort_recursivo(arr, n, i + 1)

    def toString(self): 
        return "Método Selection Sort"
