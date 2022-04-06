class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        ht = defaultdict(int)
        for n in arr:
            ht[n] += 1
        def twosum(l,target):
            res = []
            r = len(arr)-1
            while l < r:
                L = arr[l]
                R = arr[r]
                S = L+R
                if S == target:
                    res.append([L,R])
                    while l<r and L == arr[l]:
                        
                        l += 1
                    while l <= r and R == arr[r]:
                        r -= 1
                        
                elif S > target:
                    r -= 1
                else:
                    l += 1
            return res
        res = i= 0
        while i < len(arr):
            n = arr[i]
            ts = twosum(i+1, target-n)
            c = 0
            while i < len(arr) and n == arr[i]:
                i += 1
            for x,y in ts:
                if n == x == y:
                    res += math.comb(ht[x],3)
                elif n == x:
                    res += math.comb(ht[x],2)*math.comb(ht[y],1)
                elif x == y:
                    res += math.comb(ht[n],1)*math.comb(ht[y],2)
                else:
                    res += ht[n]*ht[y]*ht[x]
                    
        return res%int(math.pow(10,9)+7)
            