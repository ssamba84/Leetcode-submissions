class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num0 = l = r = ret = 0
        for r,c in enumerate(nums):
            if c == 0:
                num0 += 1
            while num0 > k:
                if 0 == nums[l]:
                    num0 -= 1
                l += 1
            ret = max(ret, r-l+1)
        return ret