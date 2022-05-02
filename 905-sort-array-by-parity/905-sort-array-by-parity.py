class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = wi = 0
        while i < len(nums):
            if nums[i]%2 == 0:
                nums[i],nums[wi] = nums[wi],nums[i]
                wi += 1
            i += 1
        return nums