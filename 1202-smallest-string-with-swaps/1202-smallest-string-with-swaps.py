class Solution:
    def smallestStringWithSwaps(self, S: str, pairs: List[List[int]]) -> str:
        g = defaultdict(list)
        for s,e in pairs:
            g[s].append(e)
            g[e].append(s)
        #return len(g), len(S)
        totseen = set()
        def bfs(s):
            q = [s]
            seen = set()
            while len(q)> 0:
                s = q.pop(0)
                seen.add(s)
                totseen.add(s)
                for n in g[s]:
                    if n not in seen:
                        q.append(n)
            return seen
        
        rets = ['']*len(S)
        def srt(s, rets):
            s.sort()
            inp = [S[i] for i in s]
            inp.sort()
            for i in s:
                rets[i] = inp.pop(0)
            
        for i in range(len(S)):
            if i not in totseen:
                ri = bfs(i)
                srt(list(ri), rets)
                
        #print (rets)
        return ''.join(rets)