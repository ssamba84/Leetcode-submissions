class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        prevpo2 = 0
        for i in range(1,n+1):
            if i&(i-1) == 0:
                prevpo2 = i
                res[i] = 1
            else:
                res[i] = 1+res[i-prevpo2]
        return res
        