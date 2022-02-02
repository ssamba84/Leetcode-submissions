class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxret = 0
        minpri = math.inf
        for p in prices:
            minpri = min(minpri, p)
            maxret = max(maxret, p-minpri)
        return maxret