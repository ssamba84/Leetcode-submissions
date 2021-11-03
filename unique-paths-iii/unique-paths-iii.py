class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        num0s = 0
        R = len(grid)
        C = len(grid[0])
        sr = sc = -1
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    sr,sc = r,c
                if grid[r][c] == 0:
                    num0s += 1

        ret = 0
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        ht = {}
        def dfs(r,c,num0s):
            nonlocal ret
            if r < 0 or r >= R or c < 0 or c >= C or (r,c) in ht or grid[r][c] == -1:
                return
            if grid[r][c] == 2:
                if num0s == -1:
                    ret += 1
                return
            
            ht[(r,c)] = 1
            for i,j in neighbors:
                ri = r+i
                cj = c+j
                if 0 <= ri < R and 0<=cj<C:
                    dfs(ri,cj, num0s-1)
            del ht[(r,c)]
        dfs(sr,sc, num0s)
        return ret