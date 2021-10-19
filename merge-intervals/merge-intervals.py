class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key = lambda x: x[0])
        ps = pe = None 
        w = 0
        for s,e in intervals:
            if ps is None:
                ps = s
                pe = e
            else:
                if s <= pe:
                    pe = max(pe, e)
                else:
                    intervals[w] = [ps,pe]
                    ps,pe = s,e
                    w += 1
        intervals[w] = [ps,pe]
        return intervals[:w+1]