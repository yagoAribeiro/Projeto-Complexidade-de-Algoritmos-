import numpy as np
import matplotlib.pyplot as plt
import sys
import random
import time
from algorithms.search import search_base, busca_binaria as bn, busca_largura as bla, busca_linear as bli, busca_profundidade as bf
from algorithms.sort import sort_base, bubble_sort as bs, insertion_sort as iso, merge_sort as ms, selection_sort as ss, quick_sort as qs
from algorithms.tree import insertion, search, delete, tree_base as tb
#Borabill
sys.setrecursionlimit(1500)
def run(instance):
    print("\n1 - Iterativa\n2 - Recursiva")
    entrada = int(input("Selecione o número da abordagem ou qualquer outro para voltar: "))
    match(entrada):
        case 1 | 2:
            if (isinstance(instance, search_base.PlotableSearch)):
                runSearch(instance, instance.iterativeSearch if entrada == 1 else instance.recursiveSearch)
            elif (isinstance(instance, sort_base.PlotableSort)):
                runSort(instance, instance.iterativeSort if entrada == 1 else instance.recursiveSort)
            else: runTree(instance, entrada == 1)
        case _:
            pass

def runTree(instance = tb.PlotableTree, iterative = True):
    n_values = [1, 25, 50, 100, 200, 300, 400, 500, 700, 1000]
    t_values = []
    for i in range(len(n_values)):
        search_call = instance.iterativeSearch if iterative else instance.recursiveSearch
        insert_call = instance.iterativeInsert if iterative else instance.recursiveInsert
        delete_call = instance.iterativeDelete if iterative else instance.recursiveDelete
        arr = getData(n_values[i])
        if type(instance) is insertion.Insertion:
            instance = insertion.Insertion()
            arr.sort() ## Pior caso de inserção da árvore desbalanceada é inserir em ordem
            i_time = time.perf_counter()
            for value in arr: insert_call(value)
            f_time = time.perf_counter()
            d_time = 1000*(f_time-i_time)
            t_values.append(d_time)
        elif type(instance) is search.Search:
            instance = search.Search()
            arr.sort(reverse=True) ## Pior caso de busca da árvore desbalanceada é procurar em ordem até as folhas
            for value in arr: insert_call(value)
            x = getWorstCaseSearch(arr)
            i_time = time.perf_counter()
            search_call(x)
            f_time = time.perf_counter()
            d_time = 1000*(f_time-i_time)
            t_values.append(d_time)
        else:
            instance = delete.Delete()
            arr.sort(reverse=True) ## Pior caso de busca da árvore desbalanceada é procurar em ordem até as folhas
            for value in arr: insert_call(value)
            x = getWorstCaseSearch(arr)
            i_time = time.perf_counter()
            delete_call(x)
            f_time = time.perf_counter()
            d_time = 1000*(f_time-i_time)
            t_values.append(d_time)    
    ##Deleta o primeiro ponto, pois aparentemente ele dá um pico ao carregar uma classe pela primeira vez
    del n_values[0]
    del t_values[0]
    plotGraph(instance, n_values, t_values, iterative)


def runSearch(instance = search_base.PlotableSearch, searchFunc = any):
    n_values = [1, 25, 50, 100, 200, 300, 400, 500, 700, 1000]
    t_values = []
    for i in range(len(n_values)):
        arr = []
        x = None
        if (type(instance) is bf.BuscaProfundidade):
            for j in range(n_values[i]):
                neightbors = []
                for l in range(random.randint(0, j)):
                    random.seed()
                    neightbors.append(random.randint(0, n_values[i]//10+1))
                arr.append(neightbors)
            x = -1
        else: 
            arr = getData(n_values[i])
            x = getWorstCaseSearch(arr)
        i_time = time.perf_counter()
        searchFunc(x, arr) ##A única linha que importa
        f_time = time.perf_counter()
        d_time = 1000*(f_time-i_time)
        t_values.append(d_time)
    ##Deleta o primeiro ponto, pois aparentemente ele dá um pico ao carregar uma classe pela primeira vez
    del n_values[0]
    del t_values[0]
    plotGraph(instance, n_values, t_values, searchFunc == instance.iterativeSearch)

def runSort(instance = sort_base.PlotableSort, sortFunc = any):
    n_values = [25, 50, 100, 200, 300, 400, 500, 700, 1000]
    t_values = []
    for i in range(len(n_values)):
        arr = getData(n_values[i])
        arr = getWorstCaseSort(instance, arr)
        i_time = time.perf_counter()
        sortFunc(arr) ##A única linha que importa
        f_time = time.perf_counter()
        d_time = 1000*(f_time-i_time)
        t_values.append(d_time)
    ##Deleta o primeiro ponto, pois aparentemente ele dá um pico ao carregar uma classe pela primeira vez
    del n_values[0]
    del t_values[0]
    plotGraph(instance, n_values, t_values, sortFunc == instance.iterativeSort)

def getWorstCaseSearch(arr): return min(arr)-1 ##Pior caso de buscas é a busca por um elemento x não pertencente ao conjunto.
def getWorstCaseSort(instance, arr = []): ##Pior caso de ordenação depende do algoritmo
    if (type(instance) is bs.BubbleSort):
        arr.sort(reverse=True)
    elif (type(instance) is iso.InsertionSort):
        arr.sort(reverse=True)
    elif (type(instance) is ms.MergeSort): ##Complexidade de tempo similar para todos os casos
        pass
    elif (type(instance) is ss.SelectionSort): ##Complexidade de tempo similar para todos os casos
        pass
    elif (type(instance) is qs.QuickSort):##(COM MEDIANA) Complexidade de tempo similar para todos os casos
        pass
    return arr
            
def plotGraph(instance, vetx, vety, iterative = True):
    if (isinstance(instance, search_base.PlotableSearch) or isinstance(instance, sort_base.PlotableSort) or isinstance(instance, tb.PlotableTree)):
        plt.plot(vetx, vety, '--bo')
        plt.xlabel("Entrada (n)")
        plt.ylabel("Tempo (ms)")
        plt.title("Algoritmo: "+instance.toString()+(" Iterativo " if iterative else " Recursivo ")+"(Pior caso)")
        plt.grid(True)
        plt.show()
    
def getData(amount):
    arr = []
    for i in range(amount):
        arr.append(random.randint(-10000, 10000))
    return arr



##Runnable

entrada = any

class_instances = [
    bn.BuscaBinaria(),
    bla.BuscaLargura(),
    bli.BuscaLinear(),
    bf.BuscaProfundidade(),
    bs.BubbleSort(),
    iso.InsertionSort(),
    ms.MergeSort(),
    ss.SelectionSort(),
    qs.QuickSort(),
    insertion.Insertion(),
    delete.Delete(),
    search.Search(),
    ]

while(True):
    i = 0
    for class_ins in class_instances:
        if (isinstance(class_ins, search_base.PlotableSearch) or isinstance(class_ins, sort_base.PlotableSort) or isinstance(class_ins, tb.PlotableTree)):
            print(str(i+1)+" - "+str(class_ins.toString()))
        i+=1
    entrada = int(input("Selecione o número do algoritmo para executar ou qualquer outro para sair: "))
    try:
        if (entrada-1)<0: raise IndexError
        obj = class_instances[entrada-1]
    except:
        exit()
    run(class_instances[entrada-1])


