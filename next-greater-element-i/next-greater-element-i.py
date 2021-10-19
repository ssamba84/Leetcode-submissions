class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        ht = {}
        '''
        [1,3,4,2]
        
        3
        4
        '''
        for i in range(len(nums2)-1, -1, -1):
            n = nums2[i]
            if len(stk) == 0:
                stk = [n]
                ht[n] = -1
            else:
                while stk and stk[0] < n:
                    stk.pop(0)
                if len(stk) == 0:
                    stk = [n]
                    ht[n] = -1
                else:
                    ht[n] = stk[0]
                    stk = [n] + stk
        res = []
        for n in nums1:
            res.append(ht[n])
        return res