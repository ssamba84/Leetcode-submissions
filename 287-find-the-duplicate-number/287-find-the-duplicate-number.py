class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ret = -1
        for i,n in enumerate(nums):
            targetn = abs(n)-1
            if nums[targetn] < 0:
                ret = targetn+1
                break
            nums[targetn] *= -1
        for i,n in enumerate(nums):
            if n < 0:
                nums[i] *= -1
        return ret