class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        4 9 15 15
        4 9 19  
        '''
        if len(nums) == 1:
            return nums[0]
        numsc = Counter(nums)
        numsarr = list(numsc.items())
        numsarr.sort(key = lambda x:x[0])
        #print (numsarr)
        cn0 = c0 = 0
        cn0 = numsarr[0][0]
        cn1 = numsarr[1][0]
        c0 = numsarr[0][0]*numsarr[0][1]
        '''
        [(1, 1), (3, 1), (4, 1), (5, 1), (8, 1)]

        c1 5
        n 3
        co 1
        no 1
        '''
        if cn0 < cn1-1:
            c1 = numsarr[1][0]*numsarr[1][1] + c0
        else:
            c1 = max(numsarr[1][0]*numsarr[1][1], c0)
        for n,f in numsarr[2:]:
            if cn1 < (n-1):
                c1,c0 = c1+n*f,c1
                cn0,cn1 = cn1,n
            else:
                
                c1,c0 = max(n*f+c0,c1),c1
                cn1,cn0 = n,cn1
        return c1