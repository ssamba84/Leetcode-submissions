class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hts = [0]*256
        htt = [0]*256
        l = r = 0
        mlen = math.inf
        ret = ""
        def check1():
            for i in range(256):
                if htt[i] > 0:
                    if hts[i] < htt[i]:
                        return True
            return False
        def check2():
            for i in range(256):
                if htt[i] > 0:
                    if hts[i] < htt[i]:
                        return False
            return True
        for c in t:
            htt[ord(c)] += 1
        for r,c in enumerate(s):
            c = ord(c)
            hts[c] += 1
            while check2():
                #if check2():
                if mlen > (r-l+1):
                    ret = s[l:r+1]
                    mlen = r-l+1
                L = ord(s[l])
                hts[L] -= 1
                l += 1
        return ret