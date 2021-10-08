class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = r = ans = 0
        for r,n in enumerate(nums):
            if n != 1:
                l = r+1
            ans = max(ans, r-l+1)
        return ans