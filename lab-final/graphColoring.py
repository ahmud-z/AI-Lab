class GraphColoring:
    def __init__(self):
        self.V = 0
        self.numOfColors = 0
        self.color = []
        self.graph = []

    def graphColor(self, g, noc):
        self.V = len(g)
        self.numOfColors = noc
        self.color = [0] * self.V
        self.graph = g

        try:
            self.solve(0)
            print("No solution")
        except Exception as e:
            print("\nSolution exists")
            self.display()

    def solve(self, v):
        if v == self.V:
            raise Exception("Solution found")

        for c in range(1, self.numOfColors + 1):
            if self.isPossible(v, c):
                self.color[v] = c
                self.solve(v + 1)
                self.color[v] = 0

    def isPossible(self, v, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and c == self.color[i]:
                return False
        return True

    def display(self):
        textColor = [
            "",
            "RED",
            "GREEN",
            "BLUE",
            "YELLOW",
            "ORANGE",
            "PINK",
            "BLACK",
            "BROWN",
            "WHITE",
            "PURPLE",
            "VIOLET",
        ]
        print("\nColors :", end=" ")
        for i in range(self.V):
            print(textColor[self.color[i]], end=" ")

        print()


if __name__ == "__main__":
    print("Graph Coloring Algorithm Test\n")
    gc = GraphColoring()

    V = int(input("Enter number of vertices\n"))

    print("\nEnter matrix")
    graph = []
    for i in range(V):
        graph.append(list(map(int, input().split())))

    c = int(input("\nEnter number of colors"))
    gc.graphColor(graph, c)
