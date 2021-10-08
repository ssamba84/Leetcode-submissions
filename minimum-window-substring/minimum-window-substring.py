class Solution:
    def minWindow(self, s: str, t: str) -> str:
        htt = {}
        hts = {}
        for c in t:
            htt[c] = htt.get(c,0) + 1
        ret = ""
        ans = math.inf
        l = r = 0
        rem = len(htt)
        for r,c in enumerate(s):
            if c in htt:
                hts[c] = hts.get(c,0) + 1
                if htt[c] == hts[c]:
                    rem -= 1
            while rem <= 0:
                if ans > (r-l+1):
                    ans = r-l+1
                    ret = s[l:r+1]
                L = s[l]
                l += 1
                if L in htt:
                    hts[L] -= 1
                    if hts[L] < htt[L]:
                        rem += 1
            
        return ret