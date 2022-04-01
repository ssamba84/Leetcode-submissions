
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        seen = set(wordDict)
        @lru_cache(None)
        def helper(i, prefix):
            if i == len(s):
                return prefix in seen
            res = False
            if prefix in seen:
                res = helper(i+1, s[i])
            return res or helper(i+1, prefix+s[i])
        return helper(0,"")