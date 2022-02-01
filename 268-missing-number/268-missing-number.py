class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            ai = nums[i]
            if i != ai and ai < len(nums):
                nums[i],nums[ai] = nums[ai],nums[i]
            else:
                i += 1
        for i,n in enumerate(nums):
            if i != n:
                return i
        return i+1
        
            