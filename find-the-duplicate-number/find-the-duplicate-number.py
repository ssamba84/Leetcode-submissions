class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            n = nums[i]-1
            if n!=i and nums[n]!=nums[i]:
                nums[n],nums[i] = nums[i],nums[n]
            else:
                i += 1
        for i,n in enumerate(nums):
            if i != (n-1):
                return n
        