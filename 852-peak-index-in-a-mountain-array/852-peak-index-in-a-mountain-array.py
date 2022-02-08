class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l < r:
            m = (r-l)//2+l
            if arr[m-1]<arr[m]>arr[m+1]:
                return m
            if arr[m-1] < arr[m]:
                l = m
            else:
                r = m
        