class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (r-l)//2+l
            M = nums[m]
            #print (M,m)
            if nums[m] == target:
                return m
            if nums[l] <= M:
                if nums[l]<=target<=nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:#elif nums[m]<nums[r]:
                if nums[m]<=target<=nums[r]:
                    l = m+1
                else:
                    r = m-1
        print (l,r)
        return -1