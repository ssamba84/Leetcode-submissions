class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R = len(heights)
        C = len(heights[0])
        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]
        seen = {}
        q = [(-math.inf, 0,0)]
        res = 0
        while len(q) > 0:
            diff, r, c = heapq.heappop(q)
            res = max(diff, res)
            if r == R-1 and c == C-1:
                break
            seen[(r,c)] = 1
            for i,j in neighbors:
                ri = r+i
                cj = c+j
                if 0<=ri<R and 0<=cj<C and (ri,cj) not in seen:
                    heapq.heappush(q,(abs(heights[ri][cj]-heights[r][c]), ri,cj))
        return res