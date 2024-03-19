class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [(-2,-1), (-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

        visited = set([0, 0])
        queue = deque([(0, 0, 0)])

        steps = 0
        while queue:
            cx, cy, steps = queue.popleft()

            if cx == x and cy == y:
                return steps

            for dx, dy in moves:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

        return steps
