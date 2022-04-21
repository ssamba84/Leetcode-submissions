class MyHashSet:

    def __init__(self):
        self.ht = [None]*109

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        htkey = self.ht[key%109]
        if htkey is None:
            self.ht[key%109] = key
        elif isinstance(htkey,int):
            self.ht[key%109] = [htkey, key]
        else:
            htkey.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key) is False:
            return
        htkey = self.ht[key%109]
        if htkey is None:
            return
        elif isinstance(htkey,int):
            self.ht[key%109] = None
        else:
            htkey.remove(key)

    def contains(self, key: int) -> bool:
        htkey = self.ht[key%109]
        if htkey is None:
            return False
        elif isinstance(htkey,int):
            return self.ht[key%109] == key
        else:
            return  key in htkey


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)