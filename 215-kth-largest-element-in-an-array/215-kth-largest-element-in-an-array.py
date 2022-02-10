class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mnhp = []
        for i in range(k):
            heapq.heappush(mnhp, nums[i])
        for i in range(k,len(nums)):
            n = nums[i]
            if n > mnhp[0]:
                heapq.heappop(mnhp)
                heapq.heappush(mnhp, n)
        
        return mnhp[0]