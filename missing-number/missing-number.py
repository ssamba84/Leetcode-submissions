class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
             i
         0 1 2
        [0,1,3]
         
        '''
        i = 0
        while i < len(nums):
            n = nums[i]
            if n == len(nums):
                i += 1
                continue
            if n != i:
                nums[i],nums[n] = nums[n],nums[i]
            else:
                i += 1
        i = 0
        while i < len(nums):
            if i != nums[i]:
                break
            i += 1
        return i