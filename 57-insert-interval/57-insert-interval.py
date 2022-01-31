class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        w = 0
        ns,ne = newInterval
        for (i,(s,e)) in enumerate(intervals):
            if s<=ns<=e or ns<=s<=ne:
                ns = min(ns,s)
                ne = max(ne,e)
            elif ne < s:
                return intervals[:w] + [[ns,ne]] + intervals[i:]
            else:
                w += 1
        return intervals[:w] + [[ns,ne]]