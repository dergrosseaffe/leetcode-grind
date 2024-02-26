class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        moves = [(-1,0),(0,-1),(1,0),(0,1)]
        queue = deque()

        # adds all zeroes as seeds to the queue and assing +Inf to all
        # other cells
        for row in range(rows):
            for column in range(cols):
                if mat[row][column] == 0:
                    queue.append((row, column))
                else:
                    mat[row][column] = float('+Inf')

        while queue:
            x, y = queue.popleft()

            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] > mat[x][y] + 1:
                    # increases distance (from the origin cell) at 1
                    mat[nx][ny] = mat[x][y] + 1
                    queue.append((nx, ny))

        return mat
