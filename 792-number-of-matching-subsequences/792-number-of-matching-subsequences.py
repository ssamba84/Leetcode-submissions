class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        curr = trie = {}
        for c in s:
            curr[c] = {}
            curr = curr[c]
        curr['$'] = 1
        @lru_cache(None)
        def find(s):
            i = 0
            curr = trie
            while i< len(s) and '$' not in curr:
                c = s[i]
                key = list(curr.keys())[0]
                if c == key:
                    i += 1
                curr = curr[key]
            return i == len(s)
        for word in words:
            ans += 1 if find(word) else 0
        return ans