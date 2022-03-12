class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        mod = int(math.pow(10,9)+7)
        for i in range(2,n+1):
            prevreslen = (i-1)*2
            res *= (prevreslen+2)*(prevreslen+1)//2
        return res%mod