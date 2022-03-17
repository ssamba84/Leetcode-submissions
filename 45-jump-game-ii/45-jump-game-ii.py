class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        2 3 1 1 4
        0 1 2 3 4
          i
        mj = 4
        res = 1
        if mj == i
         res += 1
        mj = max(mj, i+ nums[i])
        
        '''
        res = 1
        if len(nums) < 2:
            return 0
        mr = nums[0]
        def getmaxreachable(p,c):
            ret = -math.inf
            for i in range(p,c+1):
                ret = max(ret, nums[i]+i)
            return ret
        prev = 0
        while mr < (len(nums)-1):
            nxt = getmaxreachable(prev, mr)
            prev, mr = mr, nxt
            res += 1
        return res