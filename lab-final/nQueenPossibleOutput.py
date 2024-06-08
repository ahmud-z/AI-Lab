class NQueen:
    def __init__(self, n):
        self.N = n
        self.solutions = []

    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                print(" ".join(str(x) for x in row))
            print()

    def is_safe(self, board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.N), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve_nq_util(self, board, col):
        if col >= self.N:
            self.solutions.append([row[:] for row in board])
            return

        for i in range(self.N):
            if self.is_safe(board, i, col):
                board[i][col] = 1

                self.solve_nq_util(board, col + 1)
                board[i][col] = 0

    def solve_nq(self):
        board = [[0] * self.N for _ in range(self.N)]
        self.solve_nq_util(board, 0)

        if not self.solutions:
            print(f"Solution does not exist for {self.N} queens")
            return False

        print(f"Found {len(self.solutions)} solutions for {self.N} queens")
        self.print_solutions()
        return True


if __name__ == "__main__":
    n = int(input("Number of queens to place - "))
    queen = NQueen(n)
    queen.solve_nq()
