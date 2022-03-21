class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ht = {}
        for i,c in enumerate(S):
            if c not in ht:
                ht[c] = [i,i]
            else:
                ht[c] = [ht[c][0],i]
        
        res = []
        intervals = list(ht.values())
        intervals.sort(key = lambda x: x[0])
        start, end = intervals[0]
        for s, e in intervals:
            if end < s:
                res.append(s-start)
                start = s
            end = max(end, e)
        res.append(len(S)-start)
        return res