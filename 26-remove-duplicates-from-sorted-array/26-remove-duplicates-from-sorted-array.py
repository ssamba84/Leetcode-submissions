class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        prev = None
        for i,n in enumerate(nums):
            if n != prev:
                nums[w] = n
                w += 1
            prev = n
        return w