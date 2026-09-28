class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # so we need to break down this problem into its core components. So a valid sudoku board is valid if in the row, column and square their is no number that is repeated. So what would this look like in its most basic step? This would look like i check a number against the row values and column values and then the square that we are in. and if valid we continue and if anything is not valid we return false otherwise return true. we arent testing inputs. So how might I actually go about checking these conditions? So I could 1. take a value and then iterate across the row and check if repeated if so return false if not continue. 2. Then i iterate down the column same thing. and then I could strictly bound the squares for iteration. This would be technically O(1) because everything is bounded very strictly but if this became more ambiguous it would be O(n^2)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])


        return True
