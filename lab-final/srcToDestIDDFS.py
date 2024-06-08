class IterativeDeepening:
    def __init__(self):
        self.stack = []
        self.depth = 0
        self.max_depth = 0
        self.goal_found = False
        self.path = []

    def iterative_deepening(self, adjacency_matrix, source, destination):
        self.number_of_nodes = len(adjacency_matrix) - 1
        while not self.goal_found:
            self.path = []
            self.depth_limited_search(adjacency_matrix, source, destination, [source])
            self.max_depth += 1
        print(f"\nGoal Found at depth {self.depth}")
        print("Path:", " -> ".join(map(str, self.path)))

    def depth_limited_search(self, adjacency_matrix, source, goal, current_path):
        self.stack = [source]
        self.depth = 0
        visited = [False] * (self.number_of_nodes + 1)
        visited[source] = True

        while self.stack:
            element = self.stack[-1]
            found = False
            for destination in range(1, self.number_of_nodes + 1):
                if self.depth < self.max_depth:
                    if (
                        adjacency_matrix[element][destination] == 1
                        and not visited[destination]
                    ):
                        self.stack.append(destination)
                        visited[destination] = True
                        self.depth += 1
                        current_path.append(destination)
                        if goal == destination:
                            self.goal_found = True
                            self.path = current_path.copy()
                            return
                        found = True
                        break
                else:
                    break
            if not found:
                self.stack.pop()
                if current_path:
                    current_path.pop()
                self.depth -= 1


if __name__ == "__main__":
    try:
        number_of_nodes = int(input("Enter the number of nodes in the graph: "))
        adjacency_matrix = [
            [0] * (number_of_nodes + 1) for _ in range(number_of_nodes + 1)
        ]
        print("Enter the adjacency matrix:")
        for i in range(1, number_of_nodes + 1):
            row = list(map(int, input().split()))
            for j in range(1, number_of_nodes + 1):
                adjacency_matrix[i][j] = row[j - 1]

        source = 1  # Assuming the source is always node 1
        destination = int(input("Enter the destination for the graph: "))
        iterative_deepening = IterativeDeepening()
        iterative_deepening.iterative_deepening(adjacency_matrix, source, destination)
    except ValueError:
        print("Wrong Input format")
