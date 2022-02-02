class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)-1
        '''
        [2,3,4,7,11]
                 r
                 l
               m 
         k  4
        '''
        while l <= r:
            m = (r-l)//2+l
            diff = arr[m]-1-m
            if diff < k:
                l = m+1
            else:
                r = m-1
        
            
        return l + k  