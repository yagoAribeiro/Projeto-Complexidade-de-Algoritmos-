from algorithms.search.search_base import PlotableSearch

class BuscaLargura(PlotableSearch):
    def __init__(self):
        super().__init__()

    def iterativeSearch(self, x, data=None):
        visited = set()
        queue = [] if data is None else data.copy()

        while queue:
            current = queue.pop(0)
            if current == x:
                return True
            visited.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

        return False

    def recursiveSearch(self, x, data=None):
        visited = set()
        queue = [] if data is None else data.copy()

        def bfs_recursive(x, queue, visited):
            if not queue:
                return False

            current = queue.pop(0)
            if current == x:
                return True
            visited.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

            return bfs_recursive(x, queue, visited)

        return bfs_recursive(x, queue, visited)

    def get_neighbors(self, node):
        neighbors = []
        if isinstance(node, dict):
            neighbors = list(node.keys())
        elif isinstance(node, list):
            neighbors = node

        return neighbors

    def toString(self):
        return "Busca em Largura"