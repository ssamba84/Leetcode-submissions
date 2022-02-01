class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        '''
         i
         0 1 2 3 4 5 6 7
        [2,3,3,4,8,2,7,1]
         
         ai 2
        '''
        while i < len(nums):
            ai = nums[i]-1
            if i != ai and nums[i]!=nums[ai]:
                nums[i],nums[ai] = nums[ai],nums[i]
            else:
                i += 1
        res = []
        for i,n in enumerate(nums):
            if i != (n-1):
                res.append(i+1)
        return res
            