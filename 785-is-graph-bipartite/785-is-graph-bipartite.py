class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        ht= {}
        def bfs(s):
            q = [(s,1)]
            
            while len(q):
                n,c = q.pop(0)
                if n in ht:
                    if ht[n] != c:
                        return False
                else:
                    ht[n] = c
                    for s in graph[n]:
                        q.append((s,c^1))
            return True
        for i in range(len(graph)):
            if i not in ht:
                if bfs(i) is False:
                    return False
        return True