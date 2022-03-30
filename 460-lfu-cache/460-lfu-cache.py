class LFUCache:

    def __init__(self, capacity: int):
        self.sz = capacity
        self.fmap = defaultdict(int)
        self.minfreq = 0
        self.ftoOD = defaultdict(OrderedDict)
    def disp(self):
        print (self.fmap, self.minfreq, self.ftoOD)
    def get(self, key: int) -> int:
        
        if key not in self.fmap:
            return -1
        oldFreq = self.fmap[key]
        self.fmap[key] += 1
        od = self.ftoOD[oldFreq]
        val = od[key]
        del od[key]
        if len(od) == 0:
            del self.ftoOD[oldFreq]
            if oldFreq == self.minfreq:
                self.minfreq += 1
        self.ftoOD[oldFreq+1][key] = val
        return val
    def put(self, key: int, value: int) -> None:
        if self.sz == 0:
            return 
        val = self.get(key)
        if val == -1:
            if len(self.fmap) == self.sz:
                k,_ = self.ftoOD[self.minfreq].popitem(0)
                del self.fmap[k]
                if len(self.ftoOD[self.minfreq]) == 0:
                    del self.ftoOD[self.minfreq]
            self.minfreq = 1
            self.fmap[key] = 1
            self.ftoOD[1][key] = value
        else:
            self.ftoOD[self.fmap[key]][key] = value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)