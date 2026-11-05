class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                box = (r // 3, c // 3)
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[box]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[box].add(board[r][c])
        return True