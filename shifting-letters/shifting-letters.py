class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ret = ""
        tot = sum(shifts)
        tempsum = 0
        def shift(c, n):
            return chr(ord('a')+(ord(c)-ord('a')+n)%26)
        for i in range(len(s)):
            ret += shift(s[i], tot-tempsum)
            tempsum += shifts[i]
        return ret