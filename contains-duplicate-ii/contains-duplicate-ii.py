class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ht = {}
        l = r = 0
        for r,n in enumerate(nums):
            if n in ht:
                return True
            ht[n] = 1
            if (r-l)>=k:
                del ht[nums[l]]
                l += 1
        return False