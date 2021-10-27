class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = 0
        p0 = cost[0]
        p1 = cost[1]
        while i < len(cost):
            n = cost[i]
            if i < 2:
                i += 1
                continue
            p1,p0 = min(p1,p0)+n,p1
            i += 1
        return min(p1,p0)