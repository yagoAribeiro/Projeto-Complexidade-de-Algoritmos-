"""from algorithms.search.search_base import PlotableSearch

class BuscaProfundidade(PlotableSearch):
    def __init__(self):
        super().__init__()
    
    def iterativeSearch(self, x, data=[]):
        return super().iterativeSearch(x, data)
    
    def recursiveSearch(self, x, data=[]):
        return super().recursiveSearch(x, data)
    
    def toString(self): 
        return "Busca por Profundidade"
"""
import random
import time

import matplotlib.pyplot as plt


# Implementação DFS Recursiva
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

# Implementação DFS Iterativa
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))
    return visited

# Função para gerar grafos aleatórios
def generate_graph(num_nodes, num_edges):
    graph = {i: [] for i in range(num_nodes)}
    edges = set()
    
    while len(edges) < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v and (u, v) not in edges and (v, u) not in edges:
            edges.add((u, v))
            graph[u].append(v)
            graph[v].append(u)  # Para grafo não direcionado
            
    return graph

# Função para medir o tempo de execução
def measure_time(algorithm, graph, start_node):
    start_time = time.time()
    algorithm(graph, start_node)
    return time.time() - start_time

# Função principal para conduzir o estudo experimental
def run_experiment():
    node_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # Tamanhos dos grafos
    num_edges = 1500  # Manteremos o número de arestas fixo

    recursive_times = []
    iterative_times = []

    for size in node_sizes:
        graph = generate_graph(size, num_edges)
        start_node = random.randint(0, size - 1)
        
        # Medir tempo para DFS recursiva
        recursive_time = measure_time(dfs_recursive, graph, start_node)
        recursive_times.append(recursive_time)
        
        # Medir tempo para DFS iterativa
        iterative_time = measure_time(dfs_iterative, graph, start_node)
        iterative_times.append(iterative_time)
    
    # Plotando os resultados
    plt.figure(figsize=(10, 6))
    plt.plot(node_sizes, recursive_times, label='DFS Recursiva', marker='o')
    plt.plot(node_sizes, iterative_times, label='DFS Iterativa', marker='s')
    
    plt.title('Comparação de Tempo de Execução: DFS Recursiva vs Iterativa')
    plt.xlabel('Número de Nós (Vertices)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Executar o experimento
run_experiment()
