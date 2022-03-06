class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        4 9 15 15
        4 9 19  
        '''
        if len(nums) == 1:
            return nums[0]
        ht = {}
        mx = -math.inf
        for n in nums:
            ht[n] = ht.get(n,0) + n
            mx = max(mx,n)
        inp = [0]*(mx+1)
        #ht = list(ht.items())
        #ht.sort(key = lambda x: x[0])
        for k,v in ht.items():
            inp[k] = v
        #print (inp)
        p = inp[0]
        c = max(inp[1],inp[0])
        for i,n in enumerate(inp):
            if i < 2:
                continue
            p,c = c,max(n+p, c)
        return max(c,p)