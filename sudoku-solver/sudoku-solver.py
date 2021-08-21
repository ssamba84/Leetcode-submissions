class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R = len(board)
        C = len(board[0])
        def findpossiblevals(r,c):
            ret = []
            ht = {str(i):1 for i in range(1,10)}
            for i in range(C):
                if board[r][i] != '.':
                    ht[board[r][i]] = 0
            for i in range(R):
                if board[i][c] != '.':
                    ht[board[i][c]] = 0
            rbi = (r//3)*3
            cbi = (c//3)*3
            for ri in range(rbi, rbi+3):
                for cj in range(cbi, cbi+3):
                    v = board[ri][cj]
                    if v != '.':
                        ht[v] = 0
            return [k for k,v in ht.items() if v!= 0]
        def helper(r,c):
            if r == R:
                return True
            if c == C:
                return helper(r+1,0)
            if board[r][c] != '.':
                return helper(r,c+1)
            else:
                possiblevals = findpossiblevals(r,c)
                for v in possiblevals:
                    board[r][c] = v
                    if helper(r,c+1):
                        return True
                    board[r][c] = '.'
            return False
        helper(0,0)
        