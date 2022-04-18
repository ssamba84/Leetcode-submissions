class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        ppi = nums[0]
        pi = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            ci = max(nums[i]+ppi, pi)
            pi,ppi = ci,pi
        return ci