class FirstUnique:

    def __init__(self, nums: List[int]):
        self.freqht = defaultdict(int)
        self.hp = []
        self.counter = 0
        for n in nums:
            self.add(n)
        #print (self.hp)
    def showFirstUnique(self) -> int:
        if len(self.hp):
            freq, _, res = self.hp[0]
            #print (freq, res)
            while (self.freqht[res] != 1) and self.hp and self.hp[0][-1] == res:
                freq, _, res = heapq.heappop(self.hp)
            if self.freqht[res] == 1:
                return res
            
        return -1

    def add(self, n: int) -> None:
        self.freqht[n] += 1
        
        self.counter += 1
        while self.hp and self.hp[0][-1] == n:
            heapq.heappop(self.hp)
        heapq.heappush(self.hp, (self.freqht[n], self.counter, n))
        #print (n, self.hp)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)