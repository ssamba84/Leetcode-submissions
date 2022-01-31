class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key = lambda x:x[0])
        _,pe = intervals[0]
        for s,e in intervals[1:]:
            if s<pe:
                return False
            pe = e
        return True