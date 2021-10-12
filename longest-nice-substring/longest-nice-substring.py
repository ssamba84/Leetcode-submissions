class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ht = {}
        for (i,c) in enumerate(s):
            if c not in ht:
                ht[c] = set()
            ht[c].add(i)
        S = ""
        for c in s:
            if c.islower():
                if c.upper() in ht:
                    S += c
                else:
                    S += '  '
            else:
                if c.lower() in ht:
                    S += c
                else: 
                    S += '  '
        Sarr = S.split('  ')
        #print (Sarr)
        if len(S) == len(s):
            return s
        
        res = []
        for a in Sarr:
            res.append(self.longestNiceSubstring("".join(a)))
        out = ""
        for a in res:
            if len(out) < len(a):
                out = a
        return out