class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.goal_level = 999999
        self.state = 0
        self.goal = None
        self.source = None
        self.N = 0
        self.init()

    def init(self):
        graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]
        self.N = len(graph)

        source_x = 0  # source state
        source_y = 2
        goal_x = 4  # goal state
        goal_y = 4
        self.source = Node(source_x, source_y, 0)  # init source
        self.goal = Node(goal_x, goal_y, 999999)  # init goal
        self.st_dfs(graph, self.source)

        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal.depth)
        else:
            print("Goal cannot be reached from starting block")

    def print_direction(self, m, x, y):
        directions = ["Down", "Up", "Right", "Left"]
        print(f"Moving {directions[m]} ({x}, {y})")

    def st_dfs(self, graph, u):
        graph[u.x][u.y] = 0
        for j in range(self.directions):  # calculating up, down, left and right directions
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]

            if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1:  # check the boundary conditions
                v_depth = u.depth + 1
                self.print_direction(j, v_x, v_y)
                if v_x == self.goal.x and v_y == self.goal.y:  # goal check
                    self.found = True
                    self.goal.depth = v_depth
                    return

                child = Node(v_x, v_y, v_depth)
                self.st_dfs(graph, child)
            if self.found:
                return

if __name__ == "__main__":
    dfs = DFS()
