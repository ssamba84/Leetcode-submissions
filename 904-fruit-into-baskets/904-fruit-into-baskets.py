class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ht = {}
        l = r = ret = 0
        for r,n in enumerate(fruits):
            ht[n] = ht.get(n,0) + 1
            while len(ht) > 2:
                n = fruits[l]
                ht[n] -= 1
                if ht[n] == 0:
                    del ht[n]
                l += 1
            ret = max(ret, r-l+1)
        return ret