class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x: x[0])
        ps, pe = intervals[0]
        w = 0
        for s,e in intervals[1:]:
            if ps<=s<=pe:
                pe = max(pe,e)
            elif pe < s:
                res.append([ps,pe])
                ps,pe = s,e
                w += 1
        res.append([ps,pe])
        return res