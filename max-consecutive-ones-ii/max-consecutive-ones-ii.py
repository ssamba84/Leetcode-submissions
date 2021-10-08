class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = r = ans = n0 = 0
        for r,n in enumerate(nums):
            if n == 0:
                n0 += 1
            while n0 > 1:
                n = nums[l]
                if n == 0:
                    n0 -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans