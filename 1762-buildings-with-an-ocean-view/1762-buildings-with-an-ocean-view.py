class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stk = []
        for i in range(len(heights)-1,-1,-1):
            n = heights[i]
            if stk and heights[stk[-1]]<n:
                stk.append(i)
            if not stk:
                stk.append(i)
        return stk[::-1]