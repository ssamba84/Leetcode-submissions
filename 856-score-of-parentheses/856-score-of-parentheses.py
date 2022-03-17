class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        for c in s:
            if c == '(':
                stk.append(c)
            else:
                res = 0
                if stk[-1].isdigit():
                    while stk[-1].isdigit():
                        res += int(stk.pop())
                    stk.pop()
                    stk.append(str(res*2))
                else:
                    stk.pop()
                    stk.append('1')
        res = 0
        while stk:
            res += int(stk.pop())
        return res