class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        ht = {}
        def helper(i,csum, curr):
            if csum == 0:
                ret.append(list(curr))
                return
            if i == len(candidates) or csum < 0:
                return
            if candidates[i] <= target:
                helper(i, csum-candidates[i], curr+[candidates[i]])
            helper(i+1, csum, curr)
        helper(0,target,[])
        return ret
            