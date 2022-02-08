class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (r-l)//2 + l
            if target == nums[m]:
                return m
            if target > nums[m]:
                l = m+1
            else:
                r = m-1
        return -1