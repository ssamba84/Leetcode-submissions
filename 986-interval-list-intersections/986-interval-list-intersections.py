class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i1 = i2 = 0
        while i1 < len(firstList) and i2 < len(secondList):
            s1,e1 = firstList[i1]
            s2,e2 = secondList[i2]
            if s1<=s2<=e1:
                res.append([s2,min(e1,e2)])
            elif s2<=s1<=e2:
                res.append([s1,min(e1,e2)])
            if e2>e1:
                i1 += 1
            else:
                i2 += 1
        return res