class Node:
    
    def __init__(self,key=0,val=0,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    

class ListNode:
    
    def __init__(self):
        
        self.head = Node()
        self.tail = Node(0,0,self.head,None)
        self.head.next = self.tail
        self.f = {}
    
    def removeNode(self,key):
        
        if key in self.f:
            node = self.f[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.f[key]
            return node.val
    
    def addNode(self,key,val):
        
        self.removeNode(key)
        node = Node(key,val,None,None)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self.f[key]= node
    
class FreqNode:
    
    def __init__(self):
        self.head = Node(0,math.inf,None,None)
        self.tail = Node(math.inf,math.inf,self.head,None)
        self.head.next = self.tail
        self.f= {0:self.head}
    def removeNode(self,key):
        if key not in self.f:
            return
        self.f[key].val -= 1
        if self.f[key].val == 0:
            self.f[key].prev.next = self.f[key].next
            self.f[key].next = self.f[key].prev
            del self.f[key]
    def addNode(self,key,prev):
        prev = self.f[prev]
        if key in self.f:
            self.f[key].val += 1
        else:
            node = Node(key,1,prev,prev.next)
            prev.next = node
            node.next.prev = node
            self.f[key] = node

class LFUCache:

    def __init__(self, capacity: int):
        
        self.listNodes = defaultdict(lambda : ListNode())
        self.freq = defaultdict(int)
        self.capacity = capacity
        self.freqNode = FreqNode()

    def get(self, key: int) -> int:
        if self.freq[key] == 0:
            return -1
        
        val = self.listNodes[self.freq[key]].removeNode(key)
        self.freqNode.addNode(self.freq[key]+1,self.freq[key])
        self.freqNode.removeNode(self.freq[key])
        self.freq[key] += 1
        self.listNodes[self.freq[key]].addNode(key,val)
        return val

    def put(self, key: int, value: int) -> None:
        
        if self.freq[key] == 0:
            self.capacity -= 1
        
        if self.capacity < 0:
            
            min_freq = self.freqNode.head.next.key
            self.freqNode.removeNode(min_freq)
            self.freq[self.listNodes[min_freq].head.next.key] = 0
            self.listNodes[min_freq].removeNode(self.listNodes[min_freq].head.next.key)
            self.capacity += 1
        
        self.freqNode.addNode(self.freq[key]+1,self.freq[key])
        self.freqNode.removeNode(self.freq[key])
        self.listNodes[self.freq[key]].removeNode(key)
        
        self.freq[key] += 1
        self.listNodes[self.freq[key]].addNode(key,value)
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
