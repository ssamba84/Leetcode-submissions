class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        st. en
        1 2 2 2
        2 1 3 1
        3 0 4 0
        """
        
        res = [-1]*len(intervals)
        if len(intervals) < 2:
            return res
        hps = []
        hpe = []
        for i, (s,e) in enumerate(intervals):
            heapq.heappush(hps, (s,i))
            heapq.heappush(hpe, (e,i))

        while len(hpe) > 0:
            e,ei = heapq.heappop(hpe)
            si = -1
            while len(hps) > 0 and hps[0][0]<e:
                s,si = heapq.heappop(hps)
            if len(hps) > 0:
                s,si = hps[0]
                res[ei] = si
        return res
                