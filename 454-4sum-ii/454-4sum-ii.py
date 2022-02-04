class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ht = {}
        for n1 in nums1:
            for n2 in nums2:
                sm = n1+n2
                ht[sm] = ht.get(sm,0) + 1
        res = 0
        for n3 in nums3:
            for n4 in nums4:
                sm = 0-n3-n4
                res += ht.get(sm,0)
        return res