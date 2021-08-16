class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {n:[] for n in range(numCourses)}
        inc = {n:0 for n in range(numCourses)}
        for c, pr in prerequisites:
            graph[pr].append(c)
            inc[c] += 1
        q = []
        for k,v in inc.items():
            if v == 0:
                q.append(k)
        res = []
        while len(q)>0:
            pr = q.pop(0)
            numCourses -= 1
            for c in graph.get(pr,[]):
                inc[c] -= 1
                if inc[c] == 0:
                    q.append(c)
        return 0==numCourses