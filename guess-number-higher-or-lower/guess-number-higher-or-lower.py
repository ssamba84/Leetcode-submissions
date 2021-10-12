# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            m = (r-l)//2+l
            guessm = guess(m)
            if guessm == 0:
                return m
            if guessm == 1:
                l = m+1
            else:
                r = m-1
        