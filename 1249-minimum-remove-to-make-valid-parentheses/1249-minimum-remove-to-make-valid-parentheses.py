class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        remi = []
        for i,c in enumerate(s):
            if c == '(':
                stk.append((i,c))
            elif c == ')':
                if len(stk) == 0:
                    remi.append(i)
                else:
                    _,tc = stk.pop()
        res = [c for c in s]
        for i in remi:
            res[i] = ''
        for i,_ in stk:
            res[i] = ''
        return "".join(res)
            
                