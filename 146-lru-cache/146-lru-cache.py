class Node(object):
    def __init__(self, key, val, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next
    
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.ht = {}
        self.head = self.tail = None
    def appendnode(self, node):
        if node.key == self.head.key:
            return
        if node.key == self.tail.key:
            self.tail = self.tail.prev
            self.tail.next= None
            node.next = self.head
            self.head.prev = node
            self.head= node
            return
        
        np = node.prev
        nn = node.next

        np.next = nn
        if nn is not None:
            nn.prev = np
        
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
    def get(self, key: int) -> int:
        #print ("GET", key, self.ht.keys())
        if key not in self.ht:
            return -1
        node = self.ht[key]
        self.appendnode(node)
        return node.val
    def put(self, key: int, value: int) -> None:

        if key not in self.ht:
            node = Node(key,value,prev = None, next = self.head)
            self.ht[key] = node
            if self.head is not None:
                self.head.prev = node
            else:
                self.tail = self.head = node
            self.head = node
        else:
            node = self.ht[key]
            node.val = value
            self.appendnode(node)
        if len(self.ht) > self.size:
            ln = self.tail
            del self.ht[ln.key]
            tprev = self.tail.prev
            if tprev:
                tprev.next = None
            self.tail = tprev
        #print ("PUT", key, value, self.ht.keys(), self.head, self.tail)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)