class DFS:
    graph = []
    colors = []
    discovery_time = []
    finish_time = []
    time = 0
    total_nodes = 0
    max_level = -1
    current_level = -1

    def __init__(self, graph) -> None:
        self.graph = graph
        self.total_nodes = len(graph)
        self.colors = [0] * self.total_nodes
        self.discovery_time = [99999] * self.total_nodes
        self.finish_time = [99999] * self.total_nodes
        self.time = 0

    def run(self, src, target, max_level):
        self.max_level = max_level
        self.src = src
        self.target = target

        if(src == self.target):
            return True
        
        if(self.max_level <= 0):
            return False
        
        for node in range(self.total_nodes):
            if self.colors[node] == 0:
                self.visit(node)

    def visit(self, node):
        

        self.colors[node] = 1
        self.time += 1
        self.discovery_time[node] = self.time
        self.current_level += 1

        if self.current_level < self.max_level:
            for v in range(self.total_nodes):
                if self.graph[node][v] == 1 and self.colors[v] == 0:
                    self.visit(v)
        
        self.colors[node] = 2
        self.time += 1
        self.finish_time[node] = self.time

    def result(self):
        for node in range(self.total_nodes):
            print(f"DTIME: {self.discovery_time[node]} FTIME: {self.finish_time[node]}")  


def main():
    input_matrix = []

    f = open("input_dfs.txt")
    nodes, edges = map(int, f.readline().split())

    for row in range(nodes):
        input_matrix.append([0] * nodes)

    with open("input_dfs.txt") as f:
        f.readline()

        for line in f.readlines():
            v1, v2 = map(int, line.split())
            input_matrix[v1][v2] = 1

    dfs = DFS(input_matrix)
    dfs.run(0, 3, 2)
    dfs.result()
    

if __name__ == "__main__":
    main()
