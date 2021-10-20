class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
         i 
         0 1 2 3 4 5 6 7 
        [3,3,2,4,8,2,7,1]
        n 2
        '''
        i = 0
        while i < len(nums):
            n = nums[i]-1
            
            if n != i and nums[n]!=nums[i]:
                nums[i],nums[n] = nums[n],nums[i]
            else:
                i += 1
        res = []
        for i,n in enumerate(nums):
            if n !=(i+1):
                res.append(i+1)
        return res