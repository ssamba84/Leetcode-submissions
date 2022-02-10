class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ht = {}
        ret = 0
        for n in nums:
            if k == 0:
                if n in ht and ht[n] <2:
                    ret += 1
                ht[n] = ht.get(n,0) + 1
                
            if n not in ht:
                ret += ht.get(n+k,0)
                ret += ht.get(n-k,0)
                ht[n] = 1
        return ret