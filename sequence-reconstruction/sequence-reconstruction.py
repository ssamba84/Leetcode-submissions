class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if len(org) + len(seqs) == 0:
            return True
        if len(seqs) == 0:
            return False
        graph = {}
        inc = {}
        for seq in seqs:
            if len(seq) == 1:
                if seq[0] not in graph:
                    graph[seq[0]] = set()
                    if seq[0] not in inc:
                        inc[seq[0]] = 0
            for p,c in zip(seq, seq[1:]):
                if p not in graph:
                    graph[p] = set()
                if p not in inc:
                    inc[p] = 0
                if c not in inc:
                    inc[c] = 0
                if c in graph[p]:
                    continue
                graph[p].add(c)
                inc[c] = inc.get(c,0)+1
        q= []
        res = []
        for k,v in inc.items():
            if v == 0:
                q.append(k)
        #print (graph, inc)
        while len(q) > 0:
            #print (q)
            if len(q)>1:
                return False
            c = q.pop(0)
            res.append(c)
            for k in graph.get(c,[]):
                inc[k] -= 1
                if inc[k] == 0:
                    q.append(k)
        #print(res, graph, inc)
        for k,v in inc.items():
            if v != 0:
                return False
        return (res) == (org)