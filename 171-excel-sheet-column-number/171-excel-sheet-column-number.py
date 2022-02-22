class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            c = ord(c)-ord('A') + 1
            res = res*26+c
        return res