from collections import deque

class Node:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level
        self.parent = None

class BFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.N = 0
        self.found = False
        self.goal_level = 0
        self.source = None
        self.goal = None

    def init(self):
        graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1],
        ]
        self.N = len(graph)

        source_x = 0  # source state
        source_y = 2
        goal_x = 2  # goal state
        goal_y = 4
        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, 999999)
        self.st_bfs(graph)
        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal_level)
            self.print_path()  # Call to print the path
        else:
            print("Goal can not be reached from the starting block")

    def st_bfs(self, graph):
        q = deque()
        q.append(self.source)

        while q:
            u = q.popleft()

            for j in range(self.directions):
                v_x = u.x + self.x_move[j]
                v_y = u.y + self.y_move[j]

                if (0 <= v_x < self.N) and (0 <= v_y < self.N) and graph[v_x][v_y] == 1:
                    v_level = u.level + 1
                    if v_x == self.goal.x and v_y == self.goal.y:
                        self.found = True
                        self.goal_level = v_level
                        self.goal.level = v_level
                        self.goal.parent = u  # Set parent of goal node
                        return  # Goal found, no need to continue BFS

                    graph[v_x][v_y] = 0
                    child = Node(v_x, v_y, v_level)
                    child.parent = u  # Set parent of child node
                    q.append(child)

    def print_path(self):
        path = []
        current = self.goal
        while current is not None:
            path.append((current.x, current.y))
            current = current.parent
        path.reverse()
        print("Path:", path)

def main():
    b = BFS()
    b.init()

if __name__ == "__main__":
    main()
