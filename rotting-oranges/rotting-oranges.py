class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        q = []
        numfresh = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    numfresh += 1
        ret = 0
        if numfresh == 0:
            return ret
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        qlen = len(q)
        while len(q) > 0:
            
            cqlen = qlen
            qlen = 0
            ret += 1
            for _ in range(cqlen):
                r,c = q.pop(0)
                
                for i,j in neighbors:
                    ri = r+i
                    cj = c+j
                    if ri>=0 and ri < R and cj >=0 and cj<C and grid[ri][cj] == 1:
                        grid[ri][cj] = 2
                        numfresh -= 1
                        q.append([ri,cj])
                        qlen += 1
        if numfresh == 0:
            return ret-1
        else:
            return -1