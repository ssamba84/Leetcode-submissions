class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        ht = {'(':')','{':'}','[':']'}
        for c in s:
            if c in '({[':
                stk.append(c)
            else:
                if len(stk) == 0 or c != ht[stk.pop()]:
                    return False
        return len(stk) == 0