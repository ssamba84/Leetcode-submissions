class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cstr = ""
        res = 0
        for c in s:
            if len(cstr) == 2:
                if c not in cstr and cstr[1] != cstr[0]:
                    res += 1
                cstr = cstr[1]
            cstr += c
        return res