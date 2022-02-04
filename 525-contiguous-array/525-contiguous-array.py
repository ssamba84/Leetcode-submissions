class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ht = {}
        sm = 0
        res = 0
        # 0  1  0
        # -1 0 -1
        # 
        for (i,n) in enumerate(nums):
            if n == 0:
                sm -= 1
            else:
                sm += 1
            if sm == 0:
                res = max(res, i+1)
            if sm not in ht:
                ht[sm] = i
            else:
                res = max(res, i-ht[sm])
        return res