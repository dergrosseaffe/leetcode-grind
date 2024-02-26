class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        moves = [(-1,0),(0,-1),(1,0),(0,1)]
        rows  = len(grid)
        cols  = len(grid[0])
        queue = deque()
        fresh = 0

        # adds all rotten oranges to the queue:
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        while queue and fresh:
            time += 1

            for i in range(len(queue)):
                # rots current orange and adds all adjacent fresh oranges to the queue
                row, col = queue.popleft()
                grid[row][col] = 2

                for dx, dy in moves:
                    nrow, ncol = row + dx, col + dy

                    if 0 <= nrow < rows and 0 <= ncol < cols and grid[nrow][ncol] == 1:
                        grid[nrow][ncol] = 2
                        queue.append((nrow, ncol))
                        fresh -= 1


        return time if not fresh else -1
