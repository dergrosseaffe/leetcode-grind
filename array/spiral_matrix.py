class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        moves = ((0, 1), (1, 0), (0, -1), (-1, 0))  # right, down, left, up
        i, j = 0, 0 # start position
        move_index = 0  # start moving right

        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        order = []

        while len(visited) < rows * cols:
            dx, dy = moves[move_index]

            if 0 <= i < rows and 0 <= j < cols and (i, j) not in visited:
                order.append(matrix[i][j])
                visited.add((i, j))
            else:
                # undo last move which was invalid
                i -= dx
                j -= dy
                # change direction
                move_index = (move_index + 1) % 4
                dx, dy = moves[move_index]

            i += dx
            j += dy

        return order
