class Solution:
    def reorganizeString(self, s: str) -> str:
        ht = {}
        if len(s) < 2:
            return s
        for c in s:
            ht[c] = ht.get(c,0)+ 1
        hp = []
        for k,v in ht.items():
            heapq.heappush(hp, (-v,k))
        pf,pc = heapq.heappop(hp)
        res = ""
        cc=cf=None
        '''
        pf -2
        pc  a
        res aba
        cf -2
        cc a
        -2a
        '''
        while len(hp) > 0:
            res += pc
            pf += 1
            cf,cc = heapq.heappop(hp)
            
            if pf != 0:
                heapq.heappush(hp, (pf,pc))
            pc,pf = cc,cf
        res += pc
        if len(res)!=len(s):
            return ""
        return res
            
            
            