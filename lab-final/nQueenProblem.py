class NQueen:
    def __init__(self, n):
        self.N = n

    def print_solution(self, board):
        for row in board:
            print(" ".join(str(x) for x in row))

    def is_safe(self, board, row, col):
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.N), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve_nq_util(self, board, col):
        # base case: If all queens are placed then return true
        if col >= self.N:
            return True

        # Consider this column and try placing this queen in all rows one by one
        for i in range(self.N):
            if self.is_safe(board, i, col):
                # Place this queen in board[i][col]
                board[i][col] = 1

                # recur to place rest of the queens
                if self.solve_nq_util(board, col + 1):
                    return True

                # If placing queen in board[i][col] doesn't lead to a solution
                # then remove queen from board[i][col] (BACKTRACK)
                board[i][col] = 0

        # If the queen cannot be placed in any row in this column col, then return false
        return False

    def solve_nq(self):
        board = [
            [0] * self.N for _ in range(self.N)
        ]  # create N*N grid and initialize to 0
        if not self.solve_nq_util(board, 0):
            print(f"Solution does not exist for {self.N} queens")
            return False

        print(f"Solution found for {self.N} queens")
        self.print_solution(board)
        return True


if __name__ == "__main__":
    n = int(input("Number of queens to place - "))
    queen = NQueen(n)
    queen.solve_nq()
