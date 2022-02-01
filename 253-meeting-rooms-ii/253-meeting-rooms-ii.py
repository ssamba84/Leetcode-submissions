class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        hp = []
        res = 0
        for s,e in intervals:
            while len(hp) > 0 and (hp[0])<=s:
                heapq.heappop(hp)
            heapq.heappush(hp, e)
            res = max(res, len(hp))
        return res