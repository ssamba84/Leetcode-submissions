class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        m = min([m]+[r for r,_ in ops])
        n = min([n]+[c for _,c in ops])
        return m*n