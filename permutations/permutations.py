class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for n in nums:
            newret = []
            while len(ret)>0:
                perm = ret.pop()
                for i in range(len(perm)+1):
                    newperm = perm.copy()
                    newperm.insert(i,n)
                    newret.append(newperm)
            ret = newret
        return ret
            