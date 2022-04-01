class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        if totalsum%2 != 0:
            return False
        targetsum = totalsum//2
        @lru_cache(None)
        def helper(i, currtotal):
            if currtotal == 0:
                return True
            if i == len(nums):
                return False
            ret = False
            if currtotal >= nums[i]:
                ret = helper(i+1, currtotal-nums[i])
            return ret or helper(i+1, currtotal)
        return helper(0,targetsum)