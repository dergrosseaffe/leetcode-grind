class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        seeds = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    seeds.append((i, j))

        for i, j in seeds:
            for row in range(len(matrix)):
                matrix[row][j] = 0
            for column in range(len(matrix[0])):
                matrix[i][column] = 0
