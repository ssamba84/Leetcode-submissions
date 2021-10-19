class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns,ne = newInterval
        i = w = 0
        '''
                 w
        [[1,2],[3,5],[6,7],[8,10],[12,16]]
                            s e
         ns 3
         ne 8
         
        '''

        while i < len(intervals):
            s,e = intervals[i]
            if s > ne:
                break
            if s<=ns<=e or s<=ne<=e:
                ns = min(ns,s)
                ne = max(ne,e)
            elif e < ns:
                intervals[w] = [s,e]
                w += 1
            i += 1
        return intervals[:w] + [[ns,ne]] + intervals[i:]