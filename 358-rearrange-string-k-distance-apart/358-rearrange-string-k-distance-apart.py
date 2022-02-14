class Solution:
    def rearrangeString(self, s: str, K: int) -> str:
        if K == 0:
            return s
        ht = Counter(s)
        hp = []
        for k,v in ht.items():
            heapq.heappush(hp, (-v,k))
        q = []
        ret = ""
        while len(hp) > 0:
            #if len(hp)>0:
            cv, ck = heapq.heappop(hp)
            #else:
            #    cv,ck = q.pop(0)
            ret += ck
            cv += 1
            
            q.append((cv, ck))
            if len(q) == K:
                v,k = q.pop(0)
                if v != 0:
                    heapq.heappush(hp, (v,k))
        if len(ret) == len(s):
            return ret
        return ""