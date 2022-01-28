class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        l = 0
        r = w = len(nums)-1
        while l <= r:
            L = nums[l]**2
            R = nums[r]**2
            if L > R:
                res[w] = L
                l += 1
            else:
                res[w] = R
                r -= 1
            w -= 1
        return res