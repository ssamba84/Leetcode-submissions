class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for n in nums:
            reslen =len(ret)
            for i in range(reslen):
                rescopy = ret[i].copy()
                rescopy.append(n)
                ret.append(rescopy)
        return ret