class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R = len(matrix)
        C = len(matrix[0])
        kr = int(math.ceil(R/2))
        kc = int(math.ceil(C/2))
        ri = ci = 0
        res = []
        while ri < kr and ci < kc:
            #top row
            for c in range(ci,C-ci):
                res.append(matrix[ri][c])
            #right col
            if len(res) == R*C:
                break
            for r in range(ri+1, R-ri):
                res.append(matrix[r][C-1-ci])
            #bottom row
            
            if len(res) == R*C:
                break
            for c in range(C-2-ci,ci-1,-1):
                res.append(matrix[R-1-ri][c])
            #left col
            
            if len(res) == R*C:
                break
            for r in range(R-2-ri,ri,-1):
                res.append(matrix[r][ci])
            ri += 1
            
            ci += 1
            
            if len(res) == R*C:
                break
        return res