class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = None
        for i,n in enumerate(nums):
            if prev == n:
                return True
            prev = n
        return False