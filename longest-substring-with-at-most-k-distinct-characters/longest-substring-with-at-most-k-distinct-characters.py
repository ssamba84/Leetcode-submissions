class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = r = 0
        ans = 0
        ht = {}
        for r,c in enumerate(s):
            ht[c] = ht.get(c,0) +1
            while len(ht) > k:
                c = s[l]
                ht[c] -= 1
                if ht[c] == 0:
                    del ht[c]
                l += 1
            ans = max(ans, r-l+1)
        return ans