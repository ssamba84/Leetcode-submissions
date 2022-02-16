class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k < 2:
            return len(s)
        if len(s) < k:
            return 0
        
        ht = [0]*26
        l = r = res = 0
        def check(ht):
            for n in ht:
                if n > 1:
                    return False
            return True
        for r,c in enumerate(s):
            c = ord(c)-ord('a')
            ht[c] += 1
            if (r-l+1) == k:
                if check(ht):
                    res += 1
                
                L = ord(s[l])-ord('a')
                ht[L] -= 1
                l += 1
        return res