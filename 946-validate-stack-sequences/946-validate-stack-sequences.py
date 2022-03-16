class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        popi = 0
        for n in pushed:
            stk.append(n)
            while stk and stk[-1] == popped[popi]:
                stk.pop()
                popi += 1
        if popi < len(popped) or len(stk):
            return False
        return True