class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stk = []
        for c in ops:
            #print (c,stk)
            if c.isdigit() or c[0] in '-':
                stk.append(int(c))
            elif c == 'C':
                stk.pop()
            elif c == 'D':
                stk.append(stk[-1]*2)
            else:
                stk.append(stk[-1]+stk[-2])
        return sum(stk)