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
    print(input_matrix)

    

if __name__ == "__main__":
    main()
