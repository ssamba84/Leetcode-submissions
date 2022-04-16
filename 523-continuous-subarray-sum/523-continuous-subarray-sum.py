class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ht = {}
        csum = 0
        def check(ind,csum):
            for i in range(csum//k+1):
                if csum-i*k in ht:
                    if ht[csum-i*k] <= (ind-2):
                        return True
            return False
        for i,n in enumerate(nums):
            csum += n
            if csum not in ht:
                ht[csum] = i
            if csum%k == 0 and i >= 1:
                return True
            if check(i,csum):
                return True
        return False