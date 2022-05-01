class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def reduce(S):
            ret = ""
            for c in S:
                if c == '#':
                    ret = ret[:-1]
                else:
                    ret += c
            return ret
        return reduce(s) == reduce(t)