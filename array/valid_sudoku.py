class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                digit = board[row][col]

                if digit == ".":
                    continue

                box_index = (row // 3) * 3  + col // 3
                if digit in rows[row] or digit in cols[col] or digit in boxes[box_index]:
                    return False

                rows[row].add(digit)
                cols[col].add(digit)
                boxes[box_index].add(digit)

        return True
