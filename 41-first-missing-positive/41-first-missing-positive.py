class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            ai = nums[i]-1
            if i != ai and 0<=ai<len(nums) and nums[i]!=nums[ai]:
                nums[i],nums[ai] = nums[ai],nums[i]
            else:
                i += 1
        i = 0
        while i < len(nums):
            ai = nums[i]-1
            if i != ai:
                break
            i += 1
        return i+1