class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        w = 0
        for i,n in enumerate(nums):
            if prev != n:
                nums[w] = n
                w += 1
            prev = n
        return w