class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {n:[] for n in range(numCourses)}
        inc = {n:0 for n in range(numCourses)}
        for c, pr in prerequisites:
            graph[pr].append(c)
            inc[c] += 1
        q = []
        res = []
        for k,v in inc.items():
            if v ==0:
                q.append(k)
        while len(q) > 0:
            pr = q.pop(0)
            res.append(pr)
            for c in graph[pr]:
                inc[c] -= 1
                if inc[c] == 0:
                    q.append(c)
        if len(res) == numCourses:
            return res
        return []