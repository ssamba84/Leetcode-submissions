class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        i = wi = 0
        while i < len(nums):
            n = nums[i]
            if n < target:
                nums[i],nums[wi] = nums[wi],nums[i]
                wi += 1
            i += 1
        #print (nums,wi)
        i = l = wi
        while i <len(nums):
            n = nums[i]
            if n == target:
                nums[i],nums[wi] = nums[wi],nums[i]
                wi += 1
            i += 1
        return list(range(l,wi))