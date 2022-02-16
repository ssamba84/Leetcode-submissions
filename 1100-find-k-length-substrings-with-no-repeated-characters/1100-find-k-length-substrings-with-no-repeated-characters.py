class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k < 2:
            return len(s)
        if len(s) < k:
            return 0
        
        ht = [0]*26
        l = r = res = 0

        numrepeat = 0
        for r,c in enumerate(s):
            c = ord(c)-ord('a')
            if ht[c] != 0:
                numrepeat += 1
            ht[c] += 1
            
            if (r-l+1) == k:
                if numrepeat == 0:
                    res += 1
                
                L = ord(s[l])-ord('a')
                if ht[L] > 1:
                    numrepeat -= 1
                ht[L] -= 1
                
                l += 1
        return res