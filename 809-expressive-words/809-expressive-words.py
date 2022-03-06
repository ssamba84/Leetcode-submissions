class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check(s,w):
            if len(s) < len(w):
                return False
            wi = si = 0
            while si < len(s) and wi < len(w):
                cs = s[si]
                cw = w[wi]
                wc = sc = 0
                if cs != cw:
                    return False
                while si < len(s) and cs == s[si]:
                    si += 1
                    sc += 1
                while wi < len(w) and cw == w[wi]:
                    wi += 1
                    wc += 1
                #print (cs, sc, wc)
                if wc > sc or (sc!=wc and sc < 3):
                    return False
            if wi != len(w) or si != len(s):
                return False
            return True
        ret = 0
        for word in words:
            if check(s,word):
                ret += 1
        return ret
                
                    