class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        R = len(board)
        C = len(board[0])
        def helper(r,c, ht):
            
            if board[r][c] == 'X':
                return True
            if (r == 0) or (r == (R-1)) or (c == 0) or (c == (C-1)):
                return False
            ret = True
            ht[(r,c)] = 1
            for i,j in neighbors:
                ri = r+i
                cj = c+j
                if (ri,cj) not in ht:
                    ret &= helper(ri,cj, ht)
            
            return ret
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    ht = {}
                    if helper(r,c,ht):
                        for i,j in ht.keys():
                            board[i][j] = 'X'
            