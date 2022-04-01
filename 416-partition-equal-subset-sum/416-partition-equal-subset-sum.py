class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        if totalsum%2 != 0:
            return False
        
        targetsum = totalsum//2
        dp = [[False]*(1+targetsum) for _ in range(len(nums))]
        for r in range(len(nums)):
            dp[r][0] = True
        for r in range(len(nums)):
            for c in range(1,targetsum+1):
                res = False
                if r > 0:
                    res = dp[r-1][c]
                if c >= nums[r]:
                    res = res or dp[r-1][c-nums[r]]
                dp[r][c] = res
        return dp[-1][-1]