class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c0 = cost[0]
        c1 = cost[1]
        for i in range(2,len(cost)):
            cc = min(c0, c1)+cost[i]
            c0,c1 = c1,cc
        return min(c0,c1)