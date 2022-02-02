class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        htp = [0]*26
        hts = [0]*26
        l = 0
        res = []
        for c in p:
            c = ord(c)-ord('a')
            htp[c] += 1
        for (r,c) in enumerate(s):
            c = ord(c)-ord('a')
            hts[c] += 1
            if (r-l+1) == len(p):
                if hts == htp:
                    res.append(l)
                lc = ord(s[l])-ord('a')
                hts[lc] -= 1
                l += 1
        return res