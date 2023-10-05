class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        cells = []
        for r in range(n):
            for c in range(n):
                if board[r][c] != '.':
                    num = int(board[r][c])
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + c // 3].add(num)
                else:
                    cells.append((r, c))

        def backtrack(i=0):
            if i == len(cells):
                return True 
            r, c = cells[i]
            index = (r // 3) * 3 + c // 3
            for num in range(1, 10):
                if (
                    num not in rows[r]
                    and num not in cols[c]
                    and num not in boxes[index]
                ):
                    board[r][c] = str(num)
                    
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[index].add(num)
                    if backtrack(i + 1):
                        return True
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[index].remove(num)

            return False 
        backtrack()