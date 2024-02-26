class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = [(-1,0), (0,-1), (1,0), (0,1)]
        rows = len(grid)
        cols = len(grid[0])

        def visitAll(row: int, col: int) -> None:
            if (row < 0 or row >= rows or col < 0 or col >= cols):
                return

            if (grid[row][col] != '1'):
                return

            grid[row][col] = '#'

            for dx, dy in moves:
                visitAll(row+dx, col+dy)

        numIslands = 0
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if (grid[i][j] == '1'):
                    numIslands += 1
                    visitAll(i, j)

        return numIslands
