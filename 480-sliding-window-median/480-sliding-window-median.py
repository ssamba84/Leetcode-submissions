class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        mxhp = []
        mnhp = []
        res = []
        l = r = 0
        def adjustsize():
            if len(mxhp) > (len(mnhp) + 1):
                heapq.heappush(mnhp, -heapq.heappop(mxhp))
            elif len(mnhp) > len(mxhp):
                heapq.heappush(mxhp, -heapq.heappop(mnhp))
        for r,n in enumerate(nums):
            n = float(n)
            if len(mxhp) == 0 or n < -mxhp[0]:
                heapq.heappush(mxhp, -n)
            else:
                heapq.heappush(mnhp, n)
            adjustsize()
            if (r-l+1) == k:
                if len(mnhp) == len(mxhp):
                    res.append((mnhp[0]-mxhp[0])/2)
                else:
                    res.append(-mxhp[0])
                L = nums[l]
                l += 1
                if L <= -mxhp[0]:
                    mxhp.remove(-L)
                    heapq.heapify(mxhp)
                else:
                    mnhp.remove(L)
                    heapq.heapify(mnhp)
                adjustsize()
        return res