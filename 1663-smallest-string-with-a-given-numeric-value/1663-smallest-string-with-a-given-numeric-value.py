class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a']*n
        i = n-1
        k -= n
        while k > 0:
            if k < 25:
                res[i] = chr(ord(res[i])+k)
                k = 0
            else:
                f = k//25
                res[i-f+1:] = ['z']*f
                k -= f*25
                i -= f
        return "".join(res)