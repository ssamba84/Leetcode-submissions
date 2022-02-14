class Solution:
    def rearrangeString(self, s: str, K: int) -> str:
        '''
        aabbcc
        '''
        if K == 0:
            return s
        sc = Counter(s)
        q = []
        hp = []
        for k,c in sc.items():
            heapq.heappush(hp, (-c,k))
        
        res = ""
        while len(hp) > 0:
            c,k = heapq.heappop(hp)
            res += k
            c += 1
            q.append((c,k))
            if len(q) == K:
                c,k = q.pop(0)
                if c != 0:
                    heapq.heappush(hp,(c,k))
        if len(res) == len(s):
            return res
        return ""