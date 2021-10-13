class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wht = {}
        l = wlen = twlen = 0
        for word in words:
            wht[word] = wht.get(word,0) + 1
            wlen = len(word)
            twlen += wlen
        res = []
        for r,c in enumerate(s):
            cht = {}
            rem = len(wht)
            if (r-l+1) == twlen:
                for i in range(l,r+1,wlen):
                    cword = s[i:i+wlen]
                    if cword not in wht:
                        break
                    cht[cword] = cht.get(cword,0) + 1
                    if cht[cword] == wht[cword]:
                        rem -= 1
                if rem == 0:
                    res.append(l)
                l += 1
        return res