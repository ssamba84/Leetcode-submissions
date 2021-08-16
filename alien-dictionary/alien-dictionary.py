class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        ["wrt","wrf","er","ett","rftt"]
        w e
        t f
        r t
        e r
        """
        graph = {}
        inc = {}
        for word in words:
            for c in word:
                graph[c] = []
                inc[c] = 0
        for prev, word in zip(words, words[1:]):
            i = 0
            while i < len(prev) and i < len(word):
                p = prev[i]
                w = word[i]
                if p != w:
                    graph[p].append(w)
                    inc[w] += 1
                    break
                i += 1
            if i < len(prev) and i >= len(word):
                #print (i, prev, word)
                return ""
        q = []
        res = ""
        for k,v in inc.items():
            if v == 0:
                q.append(k)
        #print (q)
        while len(q) > 0:
            w = q.pop(0)
            res += w
            for c in graph.get(w,[]):
                inc[c] -= 1
                if inc[c] == 0:
                    q.append(c)
        if len(res) == len(graph):
            return res
        return ""