class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        res = [0]*2
        while i < len(nums):
            ai = nums[i]-1
            if i != ai and nums[i]!=nums[ai]:
                nums[i],nums[ai] = nums[ai],nums[i]
            else:
                i +=1
        for i,n in enumerate(nums):
            if i != (n-1):
                return [n,i+1]