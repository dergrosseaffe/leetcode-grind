class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        moves = [(-1,0), (0, -1), (0, 1), (1, 0)]

        def dfs(row: int, col: int, index: int) -> bool:
            if index == len(word): # reached limit
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if board[row][col] != word[index]:
                return False

            # marks cell as visited
            temp = board[row][col]
            board[row][col] = '#'

            found = False
            for x, y in moves:
                found = found or dfs(row+x, col+y, index+1)

            board[row][col] = temp
            return found

        # first step, looks for an initial starting point
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
