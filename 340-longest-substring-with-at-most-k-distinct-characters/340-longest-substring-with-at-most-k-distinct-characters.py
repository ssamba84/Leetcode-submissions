class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ht = {}
        l = r = ret = 0
        for r, c in enumerate(s):
            ht[c]  = ht.get(c,0) + 1
            while len(ht) > k:
                c = s[l]
                l += 1
                ht[c] -= 1
                if ht[c] == 0:
                    del ht[c]
            ret = max(ret, r-l+1)
        return ret