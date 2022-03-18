class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def helper(i,rem, curr):
            if rem == 0:
                ret.append(list(curr))
                return
            if i < 0 or i >= len(candidates):
                return
            if rem >= candidates[i]:
                helper(i, rem-candidates[i], curr+[candidates[i]])
            helper(i+1, rem, curr)
        helper(0,target, [])
        return ret