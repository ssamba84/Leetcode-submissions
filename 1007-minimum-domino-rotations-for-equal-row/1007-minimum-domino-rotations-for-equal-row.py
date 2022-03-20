class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def helper(val, s, d):
            diff = 0
            for i in range(len(s)):
                if s[i] != val:
                    if d[i] == val:
                        diff += 1
                    else:
                        return math.inf
            return diff
        res = -1
        res = min(helper(tops[0], tops, bottoms), helper(tops[0], bottoms, tops), helper(bottoms[0], tops, bottoms), helper(bottoms[0], bottoms, tops))
        return res if res != math.inf else -1