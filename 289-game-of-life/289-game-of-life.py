class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R = len(board)
        C = len(board[0])
        ht = {}
        neighbors = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
        def countlives(r,c):
            alive = dead = 0
            for i,j in neighbors:
                ri = r+i
                cj = c+j
                if ri >= 0 and ri < R and cj >= 0 and cj < C:
                    if board[ri][cj] == 0:
                        dead += 1
                    else:
                        alive += 1
            return (alive,dead)
        for r in range(R):
            for c in range(C):
                a,d = countlives(r,c)
                if board[r][c] == 1:
                    if a < 2 or a > 3:
                        ht[(r,c)] = 0
                elif board[r][c] == 0:
                    if a == 3:
                        ht[(r,c)] = 1
        for r,c in ht.keys():
              board[r][c] = ht[(r,c)]
        