class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def helper(l,r):
            if l > r:
                return 0
            apicksl = max(helper(l+2, r), helper(l+1, r-1))+ piles[l]
            apicskr = max(helper(l+1, r-1), helper(l, r-2))+  piles[r]
            return max(apicksl, apicskr)
        asum = helper(0,len(piles)-1)
        totsum = sum(piles)
        #print (asum, totsum)
        if asum > totsum//2:
            return True
        return False