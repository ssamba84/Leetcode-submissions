class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i:[] for i in range(1,n+1)}
        inc = {i:0 for i in range(1,n+1)}
        for pc, nc in relations:
            graph[pc].append(nc)
            inc[nc] += 1
        q = []
        for k,v in inc.items():
            if v == 0:
                q.append((k,1))
        res = -1
        
        while len(q) > 0:
            c, s = q.pop(0)
            #print (c)
            res = s
            n -= 1
            for nc in graph.get(c,[]):
                inc[nc] -= 1
                if inc[nc] == 0:
                    q.append((nc,s+1))
        if n == 0:
            return res
        return -1