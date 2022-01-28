class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0 = i = 0
        i2 = len(nums)-1
        while i <= i2:
            n = nums[i]
            if n == 0:
                nums[i0],nums[i] = nums[i], nums[i0]
                i0 += 1
                i += 1
            elif n == 2:
                nums[i2],nums[i] = nums[i],nums[i2]
                i2 -= 1
            else:
                i += 1
