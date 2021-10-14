class Solution:
    def numSquares(self, n: int) -> int:
        ht = [0]*(n+1)
        ht[1] = 1
        pfs = {}
        pfs[1] = 1
        for i in range(2,n+1):
            sq = math.pow(i,0.5)
            if (sq-int(sq)) == 0:
                ht[i] = 1
                pfs[i] = 1
                continue
            ns = i
            
            for k in pfs.keys():
                ns = min(ns, ht[i-k]+1)
            
            ht[i] = ns
        return ht[-1]
        