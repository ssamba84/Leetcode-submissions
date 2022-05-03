class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*len(text1)  for _ in range(len(text2))]
        for r in range(len(text2)):
            for c in range(len(text1)):
                res = 0
                if c > 0:
                    res = max(res,dp[r][c-1])
                if r > 0:
                    res = max(res,dp[r-1][c])
                if text2[r] == text1[c]:
                    if r > 0 and c > 0:
                        res = max(res,1+ dp[r-1][c-1])
                    else:
                        res = max(res,1)
                dp[r][c] = res
        return dp[-1][-1]