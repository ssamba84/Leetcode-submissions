class HitCounter:

    def __init__(self):
        self.hp = []

    def hit(self, timestamp: int) -> None:
        heapq.heappush(self.hp, timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hp and (timestamp-self.hp[0]) >= 300:
            heapq.heappop(self.hp)
        return len(self.hp)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)