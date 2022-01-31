class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        '''
        [2,-1,1,2,2]
        '''
        def getnexti(i, dirn):
            nxti = (nums[i]+i)%len(nums)
            nxtdirn = nums[nxti] > 0
            if dirn != nxtdirn:
                return -1
            if nxti == i:
                return -1
            return nxti
        def hascycle(i):
            slow = fast = i
            fwddir = nums[i] > 0
            while True:
                slow = getnexti(slow, fwddir)
                if slow == -1:
                    return False
                fast = getnexti(fast, fwddir)
                if fast  == -1:
                    return False
                fast = getnexti(fast, fwddir)
                if fast == -1:
                    return False
                if slow == fast:
                    return True
                
        for i in range(len(nums)):
            if hascycle(i):
                return True
        return False