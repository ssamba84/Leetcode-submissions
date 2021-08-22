class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
        seen = {}
        def dfs(n, prev):
            #print (n,prev, seen)
            if n in seen:
                return False
            seen[n] = 1
            for e in graph[n]:
                if e != prev:
                    if dfs(e,n) is False:
                        return False
            return True
        if dfs(0, None) is False:
            return False
        return len(seen) == n
        