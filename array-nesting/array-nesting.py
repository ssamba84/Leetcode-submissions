class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def helper(n):
            res = 0
            while 0<=n< len(nums) and n!=nums[n]:
                pn = n
                n = nums[n]
                nums[pn] = -1
                res += 1
            return res-1
        res = 1
        for i in range(len(nums)):
            res = max(res, helper(i))
        return res