class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def findsplits(maxsum):
            currsum = splits = 0
            for n in nums:
                if (currsum+n) > maxsum:
                    splits += 1
                    currsum = n
                else:
                    currsum += n
            return splits+1
        l = max(nums)
        r = sum(nums)
        ans = -1
        while l <= r:
            mid = (r-l)//2+l
            splits = findsplits(mid)
            
            if splits <= m:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans