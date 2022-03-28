class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        targetlen = l1 = l2 = prev = None
        if total_len%2 == 1:
            targetlen = total_len//2
        else:
            l1, l2 = total_len//2-1, total_len//2
        i1 = i2 = 0
        i = -1
        print (l1,l2)
        def getn(arr, i):
            if i<len(arr):
                return arr[i]
            return math.inf
        
        while i1  < len(nums1) or i2 < len(nums2):
            n1 = getn(nums1, i1)
            n2 = getn(nums2, i2)
            if n1 <= n2:
                curr = n1
                i1 += 1
            else:
                curr = n2
                i2 += 1
            i += 1
            if targetlen == i:
                return curr
            if l1 == i:
                prev = curr
            if l2 == i:
                return (curr+prev)/2
            