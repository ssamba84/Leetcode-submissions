class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        '''
        [0,3,2,1]
             p a
         
         isinc F
        '''
        if len(arr) < 3:
            return False
        if arr[0] >= arr[1]:
            return False
        prev = arr[0]
        isinc = True
        for a in arr[1:]:
            if prev == a:
                return False
            if isinc:
                if prev > a:
                    isinc = False
            else:
                if prev <= a:
                    return False
            prev = a
        return not isinc