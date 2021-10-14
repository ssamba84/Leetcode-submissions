class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        maxdiff = math.inf
        res = 0
        def twosum(l,r,target):
            maxdiff = math.inf
            res = math.inf
            while l < r:
                L = nums[l]
                R = nums[r]
                sm = L+R
                if sm == target:
                    return sm
                diff = abs(target-sm)
                if diff < maxdiff:
                    maxdiff = diff
                    res = sm
                if sm > target:
                    r -= 1
                else:
                    l += 1
            return res
                
        for i,n in enumerate(nums):
            ts = twosum(i+1, len(nums)-1, target-n)
            diff = abs(target-(ts+n))
            if diff < maxdiff:
                maxdiff = diff
                res = ts+n
        return res