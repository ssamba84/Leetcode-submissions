class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def helper(ob,cb,s):
            if (ob + cb) == 0:
                ret.append(s)
                return
            if ob > 0:
                helper(ob-1, cb, s+'(')
            if cb > ob:
                helper(ob, cb-1, s+')')
        helper(n,n,"")
        return ret