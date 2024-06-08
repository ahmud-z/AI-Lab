class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.N = len(graph)
        self.visited = [[False for _ in range(self.N)] for _ in range(self.N)]
        self.stack = []
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]

    def is_valid(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N and not self.visited[x][y] and self.graph[x][y] == 1

    def dfs(self, x, y):
        self.visited[x][y] = True

        for i in range(4):
            new_x = x + self.x_move[i]
            new_y = y + self.y_move[i]

            if self.is_valid(new_x, new_y):
                self.dfs(new_x, new_y)

        self.stack.append((x, y))

    def topological_sort(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.graph[i][j] == 1 and not self.visited[i][j]:
                    self.dfs(i, j)

        topo_order = []
        while self.stack:
            topo_order.append(self.stack.pop())

        return topo_order

if __name__ == "__main__":
    graph = [
        [0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1]
    ]

    g = Graph(graph)
    topological_order = g.topological_sort()
    print("Topological order of nodes traversal:")
    for node in topological_order:
        print(node)
