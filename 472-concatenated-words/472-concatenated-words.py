class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        seen = set(words)
        @lru_cache(None)
        def check(word, i, prefix):
            suffix = word[i+1:]
            
            if i == len(word):
                return  prefix in seen
            res = False
            if prefix in seen:
                res = check(word, i+1, word[i])
            ret =  check(word, i+1, prefix+word[i]) or res
            
            return ret
        ret = []
        for word in words:
            seen.remove(word)
            if check(word, 0, ""):
                
                ret.append(word)
            seen.add(word)
        return ret
                