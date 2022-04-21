class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        f0 = 0
        f1 = 1
        for i in range(2,n+1):
            f1,f0 = f1+f0,f1
        return f1