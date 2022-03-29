class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.pre = None
        self.next = None

class DLL:
    def __init__(self):
        self.len = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.next = self.head

    def addToHead(self, node):
        temp = self.head.next
        self.head.next = node
        node.pre = self.head
        temp.pre = node
        node.next = temp
        self.len +=1

    def removeNode(self, node):
        tempPre = node.pre
        tempNext = node.next 
        tempPre.next = tempNext
        tempNext.pre = tempPre
        self.len -=1

    def removeFromTail(self):
        currNode = self.tail.pre
        self.removeNode(currNode)
        return currNode
        
class LFUCache:

    def __init__(self, capacity: int):
        self.keyToNode = defaultdict(Node)  
        self.freqToDLL = defaultdict(DLL)
        self.capacity = capacity
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        # find the current node
        currNode = self.keyToNode[key]
        currFreq = currNode.freq
        currDLL = self.freqToDLL[currFreq]
        #remove node from currDLL
        currDLL.removeNode(currNode)
        
        # if after remove, currDLL become empty, remove it from map freqToDLL
        if currDLL.len == 0:
            del self.freqToDLL[currFreq]
            
        #update minFreq if needed
        if self.minFreq not in self.freqToDLL:
            self.minFreq +=1
        
        #update Node's freq
        currNode.freq +=1
        #get newDLL (if newfreq not exist, it will new a DLL)
        newDLL = self.freqToDLL[currNode.freq] #default value if DLL with len = 1
        #add node to front of new node
        newDLL.addToHead(currNode)
        
        return currNode.value
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        
        # if already exist, update the value
        if key in self.keyToNode:
            currNode = self.keyToNode[key]
            currNode.value = value
            #don't forget to call get()
            self.get(key)
        else:
            #if not exit, fist create a new Node
            currNode = Node(key, value)

            #add node to head of currDLL (which is self.freqToDLL[1])
            currDLL = self.freqToDLL[1]
            currDLL.addToHead(currNode)

            #add node to self.keyToNode[key]
            self.keyToNode[key] = currNode

            #if adding this make over capacity: the size of len(key)== capacity +1, remove from old minFreq's dll's tail
            if len(self.keyToNode) == self.capacity+1:
                lfuDLL = self.freqToDLL[self.minFreq]
                lruNode = lfuDLL.removeFromTail()
                del self.keyToNode[lruNode.key]


            self.minFreq = 1