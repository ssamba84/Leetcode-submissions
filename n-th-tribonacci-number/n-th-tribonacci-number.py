class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = t2 = 1
        if n < 2:
            return n
        for _ in range(n-2):
            t2,t1,t0 = t2+t1+t0, t2, t1
        return t2