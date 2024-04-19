class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        max_size = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    if row == 0 or col == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                    max_size = max(max_size, dp[row][col])

        return max_size * max_size
