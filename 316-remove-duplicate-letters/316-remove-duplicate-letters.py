class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ht = {c:i for i,c in enumerate(s)}
        stk = []
        for i,c in enumerate(s):
            if c in stk:
                continue
            while stk and stk[-1] > c and ht[stk[-1]] > i:
                stk.pop()
            stk.append(c)
        return "".join(stk)