class BuscaProfundidade(PlotableSearch):
    def __init__(self):
        super().__init__()

    def iterativeSearch(self, x, data=[]):
        return super().iterativeSearch(x, data)

    def recursiveSearch(self, x, data=[]):
        return super().recursiveSearch(x, data)

    def toString(self):
        return "Busca por Profundidade"
#implemetado busca_profundidade
def generate_graph(num_nodes, num_edges):
    graph = {i: [] for i in range(num_nodes)}
    edges = set()
    while len(edges) < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v and (u, v) not in edges and (v, u) not in edges:
            edges.add((u, v))
            graph[u].append(v)
            graph[v].append(u)
    return graph

def measure_time(algorithm, graph, start_node):
    start_time = time.time()
    algorithm(start_node, graph)
    return time.time() - start_time
