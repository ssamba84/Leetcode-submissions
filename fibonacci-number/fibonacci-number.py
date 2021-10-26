class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        f0 = 0
        f1 = 1
        for _ in range(n-1):
            f1,f0 = f1+f0, f1
        return f1
        