class UndergroundSystem:

    def __init__(self):
        self.cid2st = {}
        self.st2end = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cid2st[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startst,sttime = self.cid2st[id]
        tott, totn = self.st2end.get((startst, stationName),(0,0))
        self.st2end[(startst, stationName)] = (tott+(t-sttime), 1+totn)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tott, totn = self.st2end.get((startStation, endStation),(0,1))
        return tott/totn

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)