class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1]*len(s) for _ in range(len(s)) ]
        def helper(l,r):
            if l > r:
                return 0
            if l == r:
                dp[l][r] = 1
                return 1
            if dp[l][r] == -1:
                if s[l] == s[r]:
                    dp[l][r] = 2+ helper(l+1,r-1)
                else:
                    dp[l][r] = max(helper(l+1,r), helper(l,r-1))
            return dp[l][r]
        res = helper(0,len(s)-1)
        #print (dp)
        return res