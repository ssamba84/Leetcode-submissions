class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(i, load):
            if i >= len(nums):
                return load
            return max(helper(i+2, load+nums[i]), helper(i+1, load))
        return helper(0,0)