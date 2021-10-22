class Solution:
    def frequencySort(self, s: str) -> str:
        ht = {}
        for c in s:
            if c not in ht:
                ht[c] = (c,0)
            _,n = ht[c]
            ht[c] = (c,n+1)
        vals = list(ht.values())
        vals.sort(key = lambda x: -x[1])
        res = ""
        for c,n in vals:
            res += c*n
        return res