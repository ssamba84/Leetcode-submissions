class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ht = {}
        sm = res = 0
        for n in nums:
            sm += n
            if sm == k:
                res += 1
            res += ht.get(sm-k,0)
            ht[sm] = ht.get(sm,0) + 1
        return res