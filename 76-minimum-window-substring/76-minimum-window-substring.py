class Solution:
    def minWindow(self, s: str, t: str) -> str:
        rem = l = r = 0
        mxlen = math.inf
        res = ""
        hts = [0]*256
        htt = [0]*256
        for c in t:
            c = ord(c)
            if htt[c] == 0:
                rem += 1
            htt[c] += 1
        for (r,c) in enumerate(s):
            c = ord(c)
            if htt[c] == 0:
                continue
            hts[c] += 1
            if hts[c] == htt[c]:
                rem -= 1
            while rem == 0:
                L = ord(s[l])
                if mxlen > (r-l+1):
                    mxlen = (r-l+1)
                    res = s[l:r+1]
                if htt[L] != 0:
                    hts[L] -= 1
                    if hts[L] < htt[L]:
                        rem += 1
                l += 1
        return res