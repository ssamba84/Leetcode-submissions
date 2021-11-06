class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        1   1 
        2  10
        3  11
        5 101
          110 
         10
         11
        '''
        mask = 0
        for n in nums:
            mask ^= n
        pos1 = 1
        mcopy = mask
        while mcopy:
            if mcopy&pos1:
                break
            pos1 = pos1<<1
        n1 = 0
        for n in nums:
            if n&pos1:
                n1 ^= n
        return [n1, mask^n1]