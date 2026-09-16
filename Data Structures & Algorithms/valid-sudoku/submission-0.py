class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for sudoku to be valid, we need to check all rows, all cols, and all squares

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == ".":
                    continue
                if ( digit in rows[r]
                    or digit in cols[c]
                    or digit in squares[(r//3, c//3)] ):
                    return False
                else:
                    cols[c].add(digit)
                    rows[r].add(digit)
                    squares[(r//3, c//3)].add(digit)

        return True