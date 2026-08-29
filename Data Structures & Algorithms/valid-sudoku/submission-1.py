
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # Fixed variable name

        # Loop through every cell on the 9x9 board
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Skip empty cells
                if val == ".":
                    continue

                box_coord = (r // 3, c // 3)

                # Check for duplicates across Row, Column, and 3x3 Box
                if (
                    val in rows[r]
                    or val in cols[c]
                    or val in boxes[box_coord]
                ):
                    return False

                # Record number in tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_coord].add(val)

        return True


        