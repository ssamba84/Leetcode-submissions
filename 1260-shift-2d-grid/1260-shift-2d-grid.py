class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        if k == 0:
            return grid
        R = len(grid)
        C = len(grid[0])
        k = k%(R*C)
        if k == 0:
            return grid
        def getrc(n):
            return n//C-1,n%C
        def rev(l,r):
            while l < r:
                lr,lc = getrc(l)
                rr,rc = getrc(r)
                #print (l,r,lr,lc,rr,rc)
                grid[lr][lc],grid[rr][rc] = grid[rr][rc], grid[lr][lc]
                l += 1
                r -= 1
        n = (R*C)-1
        rev(0,n)
        #print (grid)
        #return grid
        rev(0,k-1)
        rev(k,n)
        return grid
            