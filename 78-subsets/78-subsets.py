class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            rlen = len(res)
            for i in range(rlen):
                r = res[i]
                res.append(r+[n])
        return res