class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = [0]*len(nums)
        l = 0
        w = r = len(nums)-1
        
        while l <= r:
            L = nums[l]**2
            R = nums[r]**2
            if L > R:
                ret[w] = L
                l += 1
            else:
                ret[w] = R
                r -= 1
            w -= 1
        return ret