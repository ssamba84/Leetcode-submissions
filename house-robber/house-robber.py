class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        maxret[i] = max(nums[i]+maxret[i-2], maxret[i-1])
        """
        if len(nums) == 0:
            return 0
        if len(nums)< 3:
            return max(nums)
        helper = [0]*len(nums)
        helper[0] = nums[0]
        helper[1] = max(nums[:2])
        for i,n in enumerate(nums):
            if i > 1:
                helper[i] = max(helper[i-2]+n, helper[i-1])
        return helper[-1]