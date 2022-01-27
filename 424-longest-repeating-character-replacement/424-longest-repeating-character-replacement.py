class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = ret = 0
        ht = {}
        def check():
            mx = max(ht.values())
            sm = sum(ht.values())
            return (sm-mx)>k
        for r,c in enumerate(s):
            ht[c] = ht.get(c,0) + 1
            while check():
                L = s[l]
                ht[L] -= 1
                if ht[L] == 0:
                    del ht[L]
                l += 1
            ret = max(ret, r-l+1)
        return ret