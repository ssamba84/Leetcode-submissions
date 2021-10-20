class Solution:
    def reverseWords(self, s: str) -> str:
        ret = [c[::-1] for c in s.split()]
        return " ".join(ret)[::-1]
        