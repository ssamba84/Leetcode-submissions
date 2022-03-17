class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = 2
        f1 = 3
        if n < 4:
            return n
        for i in range(4,n+1):
            f0,f1 = f1,f1+f0
        return f1