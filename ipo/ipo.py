class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        cphp = []
        php = []
        for p,c in zip(profits, capital):
            heapq.heappush(cphp, (c,p))
        for i in range(k):
            while len(cphp) and cphp[0][0] <= w:
                c,p = heapq.heappop(cphp)
                heapq.heappush(php, -p)
            if len(php) > 0:
                w += -heapq.heappop(php)
        return w