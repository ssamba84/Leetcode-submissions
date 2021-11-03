class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        R = len(board)
        C = len(board[0])
        visited = {}
        def visit(r,c):
            q = [(r,c)]
            while len(q) > 0:
                r,c = q.pop(0)
                visited[(r,c)] = 1
                for i,j in neighbors:
                    ri = r+i
                    cj = c+j
                    if 0 <= ri < R and 0 <= cj < C and (ri,cj) not in visited:
                        if board[ri][cj] == 'O':
                            visit(ri,cj)
        for r in range(R):
            if (r,0) not in visited and board[r][0] == 'O':
                visit(r,0)
            if (r,C-1) not in visited and board[r][C-1] == 'O':
                visit(r,C-1)
        for c in range(C):
            if (0,c) not in visited and board[0][c] == 'O':
                visit(0,c)
            if (R-1,c) not in visited and board[R-1][c] == 'O':
                visit(R-1,c)
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'
