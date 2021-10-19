class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = ['']*len(s)
        l = 0
        r = len(s)-1
        while l <= r:
            L = s[l]
            R = s[r]
            if L.isalpha() is False:
                res[l] = L
                l += 1
                continue
            if R.isalpha() is False:
                res[r] = R
                r -= 1
                continue
            res[l] = R
            res[r] = L
            l += 1
            r -= 1
        #print (res)
        return "".join(res)
            