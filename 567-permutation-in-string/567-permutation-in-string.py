class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ht1 = [0]*26
        ht2 = [0]*26
        for c in s1:
            c = ord(c)-ord('a')
            ht1[c] += 1
        l = r = 0
        for r,c in enumerate(s2):
            c = ord(c)-ord('a')
            ht2[c] += 1
            if (r-l+1) == len(s1):
                if ht1 == ht2:
                    return True
                L = ord(s2[l])-ord('a')
                ht2[L] -= 1
                l += 1
        return False