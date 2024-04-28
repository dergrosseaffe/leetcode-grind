class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        moves = [(-1,0),(0,-1),(0,1),(1,0)]

        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]


        def dfs(row, col):
            if memo[row][col] != 0:
                return memo[row][col]

            best = 1
            for dx, dy in moves:
                nx, ny = row + dx, col + dy

                if 0 <= nx < m and 0 <= ny < n:
                    if matrix[nx][ny] > matrix[row][col]:
                        best = max(best, 1 + dfs(nx, ny))

            memo[row][col] = best
            return best


        longest = 0
        for row in range(m):
            for col in range(n):
                if memo[row][col] == 0:
                    longest = max(longest, dfs(row, col))

        return longest
