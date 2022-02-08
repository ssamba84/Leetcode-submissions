class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        while l < r:
            m = (r-l)//2+l
            M = nums[m]
            if M == target:
                return m
            if M < target:
                l = m+1
            else:
                r = m
        return l