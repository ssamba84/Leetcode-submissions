class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        csum = 0
        l =  0
        ret = math.inf
        '''
        [2,3,1,2,4,3]
                 r
             l
         c 7
         ret 4
        '''
        for r,n in enumerate(nums):
            csum += n
            while csum >= target:
                ret = min(ret, r-l+1)
                csum -= nums[l]
                l += 1
        return ret if ret!=math.inf else 0