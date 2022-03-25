class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(speed):
            res = 0
            for n in piles:
                res += math.ceil(n/speed)
            return res
        l = 1
        r = int(math.pow(10,9))
        
        while l <= r:
            m = (r-l)//2+l
            
            calc = helper(m)
            #print (m, calc)
            if calc <= h:
                r = m-1
            if calc > h:
                l = m+1
        return l
            
        