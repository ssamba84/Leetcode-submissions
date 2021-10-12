class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = r = currsum = 0
        maxavg = -math.inf
        for r,n in enumerate(nums):
            currsum += n
            if r-l+1 == k:
                maxavg = max(maxavg, currsum/k)
                currsum -= nums[l]
                l += 1
        return maxavg