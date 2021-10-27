class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
                 i
        1 3 12 0 0
          w
        """
        w = 0
        for i,n in enumerate(nums):
            if n != 0:
                nums[i],nums[w] = nums[w],nums[i]
                w += 1
        