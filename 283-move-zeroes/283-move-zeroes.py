class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        w = i = 0
        while i < len(nums):
            if nums[i]!=0:
                nums[w],nums[i] = nums[i],nums[w]
                w += 1
            i += 1
        