class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        capmh = []
        for i in range(len(profits)):
            p = profits[i]
            c = capital[i]
            heapq.heappush(capmh,(c,p))
        profmxhp = []
        res = w
        for _ in range(k):
            while len(capmh) > 0  and res >= capmh[0][0]:
                c,p = heapq.heappop(capmh)
                heapq.heappush(profmxhp, (-p))
            if len(profmxhp) > 0:
                res += -heapq.heappop(profmxhp)
        return res