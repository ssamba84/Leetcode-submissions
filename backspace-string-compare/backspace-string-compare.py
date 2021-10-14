class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getnext(s, i):
            ign = 0
            while i >= 0:
                if s[i] != '#':
                    if ign == 0:
                        return i
                    ign -= 1
                else:
                    ign += 1
                i -= 1
            return i
        si = len(s)-1
        ti = len(t)-1
        while si >= 0 and ti >= 0:
            si = getnext(s, si)
            ti = getnext(t, ti)
            if si < 0 or ti < 0:
                break
            if s[si] != t[ti]:
                return False
            si -= 1
            ti -= 1
        si = getnext(s,si)
        ti = getnext(t,ti)
        if si < 0 and ti < 0:
            return True
        return False