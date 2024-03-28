from collections import deque


class BFS:
    def __init__(self):
        self.runBFS()  # starting bfs traversal

    def runBFS(self):
        nodeAmount = 4  # number of nodes N
        graph = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]
        visited = [0] * nodeAmount  # visited array
        level = [99999] * nodeAmount  # level array

        sourceNode = 0  # source node
        visited[sourceNode] = 1  # gray
        level[sourceNode] = 0

        q = deque()
        q.append(sourceNode)

        while q:
            parentNode = q.popleft()  # this will work as parent node
            for v in range(nodeAmount):
                if (
                    graph[parentNode][v] == 1 and visited[v] == 0
                ):  # visit the child nodes v of parent node u
                    visited[v] = 1
                    level[v] = level[parentNode] + 1
                    q.append(v)
            visited[parentNode] = 2

        for i in range(nodeAmount):
            print("Node =", i, "Level =", level[i])


def main():
    b = BFS()


if __name__ == "__main__":
    main()
