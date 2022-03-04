class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0]*len(height)
        maxright = [0]*len(height)
        mxl = 0
        for (i,n) in enumerate(height):
            mxl = max(mxl, n)
            maxleft[i] = mxl
        i = len(height)-1
        mxr = 0
        while i >= 0:
            n = height[i]
            mxr = max(mxr, n)
            maxright[i] = mxr
            i -= 1
        ret = 0
        for i in range(1, len(height)-1):
            ret += max(0,min(maxleft[i], maxright[i]) - height[i])
        return ret