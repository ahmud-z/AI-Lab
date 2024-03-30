
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, v, visited, stack, depth, max_depth):
        visited[v] = True

        if depth == max_depth:
            stack.append(v)
            return True

        for i in self.graph[v]:
            if not visited[i]:
                if self.DLS(i, visited, stack, depth + 1, max_depth):
                    stack.append(v)
                    return True

        return False

    def iterative_deepening_DFS(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                for depth in range(self.V):
                    if self.DLS(i, visited, stack, 0, depth):
                        break

        while stack:
            print(stack.pop(), end=" ")

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological sorted order of the graph:")
g.iterative_deepening_DFS()

