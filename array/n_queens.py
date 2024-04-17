class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        def is_valid(row: int, col: int) -> bool:
            for other_row in range(row):
                other_col = board[other_row]
                if other_col == col or \
                   other_row - other_col == row - col or \
                   other_row + other_col == row + col:
                    return False
            return True


        def backtrack(row: int) -> None:
            if row == n:
                solution = []
                for i in range(n):
                    solution.append('.' * board[i] + 'Q' + '.' * (n - board[i] - 1))
                solutions.append(solution)
                return

            for col in range(n):
                if is_valid(row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1


        board = [-1] * n
        solutions = []
        backtrack(0)
        return solutions
