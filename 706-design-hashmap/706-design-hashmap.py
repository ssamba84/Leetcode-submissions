class MyHashMap:

    def __init__(self):
        self.ht = [[] for _ in range(109)]

    def put(self, key: int, value: int) -> None:
        l = self.ht[key%109]
        self.remove(key)
        l.append((key,value))

    def get(self, key: int) -> int:
        l = self.ht[key%109]
        for k,v in l:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        l = self.ht[key%109]
        for k,v in l:
            if k == key:
                l.remove((k,v))
                return
        return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)