class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        
        c = i = 1
        prev = nums[0]
        while i < len(nums):
            n = nums[i]
            if prev != n:
                nums[w] = prev
                w += 1
                if c > 1:
                    nums[w] = prev
                    w += 1
                c = 0
            prev = n
            i += 1
            c += 1
        nums[w] = prev
        w += 1
        if c > 1:
            nums[w] = prev
            w += 1
        return w