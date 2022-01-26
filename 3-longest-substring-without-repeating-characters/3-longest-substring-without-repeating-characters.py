class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}
        l = r = ret = 0
        for r,c in enumerate(s):
            ht[c] = ht.get(c,0) + 1
            while ht[c] == 2:
                L = s[l]
                ht[L] -= 1
                l += 1
            ret = max(ret, r-l+1)
        return ret