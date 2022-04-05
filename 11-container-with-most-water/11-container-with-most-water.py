class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        res = 0
        while l < r:
            L = height[l]
            R = height[r]
            res = max(min(L,R)*(r-l),res)
            if L < R:
                l += 1
            else:
                r -= 1
        return res