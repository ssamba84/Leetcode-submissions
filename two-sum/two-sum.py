class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i,n in enumerate(nums):
            rem = target-n
            if rem in ht:
                return [ht[rem], i]
            ht[n] = i
        
        