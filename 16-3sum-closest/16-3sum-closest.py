class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mdiff = math.inf
        i = 0
        res = 0
        nums.sort()
        def twosumclosest(l,target):
            res = mdiff = math.inf
            r = len(nums)-1
            
            while l < r:
                sm = nums[l]+nums[r]
                diff = abs(-target+sm)
                if diff < mdiff:
                    mdiff = diff
                    res = sm
                if sm == target:
                    return res
                elif sm > target:
                    r -= 1
                else:
                    l += 1
            return res
        while i < len(nums):
            n = nums[i]
            ts = twosumclosest(i+1, target-n)
            if abs(target-ts-n) < mdiff:
                res = ts+n
                mdiff =  abs(target-ts-n)
            #print (res, ts, mdiff)
            i += 1
        return res