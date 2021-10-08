class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        ht = {}
        ans = 0
        def check(ht):
            mx = max(ht.values())
            return (sum(ht.values()) - mx) > k
        for r,c in enumerate(s):
            ht[c] = ht.get(c,0) + 1
            while check(ht):
                c = s[l]
                ht[c] -= 1
                if ht[c] == 0:
                    del ht[c]
                l += 1
            ans = max(ans, r-l+1)
        return ans