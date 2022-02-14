class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        incount = {i:0 for i in range(numCourses)}
        for c, pr in prerequisites:
            graph[pr].append(c)
            incount[c] += 1
        q = []
        res = 0
        for c,prc in incount.items():
            if prc == 0:
                q.append(c)
        while len(q) > 0:
            pr = q.pop(0)
            res += 1
            for c in graph[pr]:
                incount[c] -= 1
                if incount[c] == 0:
                    q.append(c)
        return res == numCourses