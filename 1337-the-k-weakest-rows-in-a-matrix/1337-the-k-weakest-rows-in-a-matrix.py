class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        R = len(mat)
        C = len(mat[0])
        '''
           m
         0 1 2 3 4
        [1,1,0,0,0]
         l.      
            r
        '''
        def binsearch(row):
            l = 0
            r = C-1
            while l <= r:
                m = (r-l)//2+l
                if mat[row][m] == 1:
                    l = m+1
                else:
                    r = m-1
            return l
        hp = []

        for r in range(R):
            heapq.heappush(hp, (-binsearch(r),-r))
            if len(hp) > k:
                heapq.heappop(hp)
        res = []
        while hp:
            _,r = heapq.heappop(hp)
            res.append(-r)
        return res[::-1]
            