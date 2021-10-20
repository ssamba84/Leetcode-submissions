class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            n = nums[i]-1
            if n!=i and nums[n] != nums[i]:
                nums[n],nums[i] = nums[i],nums[n]
            else:
                i += 1
        res = set()
        for i,n in enumerate(nums):
            if i != (n-1):
                res.add(n)
        return res