class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        validpoints = [(abs(a-x)+abs(b-y), i, a, b) for i,(a,b) in enumerate(points) if x == a or y == b]
        
        if len(validpoints) == 0:
            return -1
        validpoints.sort(key = lambda x: (x[0],x[1]))
        return validpoints[0][1]