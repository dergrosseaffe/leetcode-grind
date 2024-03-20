class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        moves = [(0,-1),(1,0),(0,1),(-1,0)]
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    queue.append((i, j, 0))

        while queue:
            i, j, steps = queue.popleft()

            if grid[i][j] == 'X':
                continue

            if grid[i][j] == '#':
                return steps

            grid[i][j] = 'X'  # mark as visited

            for dx, dy in moves:
                nx, ny = i + dx, j + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    queue.append((nx, ny, steps + 1))

        return -1
