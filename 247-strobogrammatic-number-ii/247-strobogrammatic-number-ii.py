class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        ht = {'1':'1', '0':'0','6':'9','8':'8','9':'6'}
        
        if n%2 == 0:
            res = ['']
            sz = 0
        else:
            res = ['0','1','8']
            sz = 1
        if sz == n:
            return res
        while sz < n:
            newres = []
            for r in res:
                for k,v in ht.items():
                    newres.append(k+r+v)
            sz += 2
            res = newres
        return [r for r in res if r[0] != '0']
        