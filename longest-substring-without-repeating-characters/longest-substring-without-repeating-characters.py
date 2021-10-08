class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        ans = 0
        ht = {}
        while r < len(s):
            c = s[r]
            if c in ht:
                l = max(l,ht[c] +1)
            ht[c] = r
            ans = max(ans, r-l+1)
            r += 1
        return ans
            
            
                