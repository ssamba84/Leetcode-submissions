class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        htp = [0]*26
        hts = [0]*26
        l = r = 0
        for c in p:
            c = ord(c)-ord('a')
            htp[c] += 1
        res = []
        for r, c in enumerate(s):
            c = ord(c)-ord('a')
            hts[c] += 1
            if r-l+1 == len(p):
                if htp == hts:
                    res.append(l)
                c = ord(s[l])-ord('a')
                hts[c] -= 1
                l += 1
        return res