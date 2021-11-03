class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = [[]]
        '''
        1 2 2
        [] [1] [12] [2]
        '''
        prevlen = len(ret)
        prev = None
        for n in nums:
            if n != prev:
                start = 0
                
            else:
                start = prevlen
            end = len(ret)
            prev = n
            prevlen = end
            for i in range(start, end):
                scopy = ret[i].copy()
                scopy.append(n)
                ret.append(scopy)
            
        return ret
                