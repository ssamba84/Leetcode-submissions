class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        hp = []
        intervals.sort(key = lambda x: x[0])
        res = 0
        print (intervals)
        for s,e in intervals:
            while hp and hp[0] <= s:
                heapq.heappop(hp)
            heapq.heappush(hp, e)
            res = max(res, len(hp))
        return res