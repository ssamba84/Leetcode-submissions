class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(s, ob, cb):
            if (ob + cb) == 0:
                res.append(s)
            else:
                if ob > 0:
                    helper(s+'(', ob-1, cb)
                if ob < cb:
                    helper(s+')', ob, cb-1)
        helper("",n,n)
        return res