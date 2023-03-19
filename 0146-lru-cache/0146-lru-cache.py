class doubleLinkedList:
    
    def __init__(self,key,val,prev=None,next=None):
        
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key
    

class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.f = defaultdict(lambda  : None)
        

    def get(self, key: int) -> int:
        
        if self.f[key]:
            
            value = self.f[key].val
            self.remove(key)
            self.add(key,value)
            
            return self.f[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        
        if self.f[key] :
            
            self.remove(key)
            self.add(key,value)
        
        elif self.capacity > 0:
            
            self.capacity -= 1
            self.add(key,value)
            
        else:
            
            self.remove(self.head.key)
            self.add(key,value)
        
#     def removeHead(self):
        
#         self.head = self.head.next
#         self.head.prev = None
    
    def remove(self,key):
        
        if self.f[key].next != None and self.f[key].prev != None:
            
            
            self.f[key].prev.next = self.f[key].next
            self.f[key].next.prev = self.f[key].prev
        
        elif self.f[key].next == None and self.f[key].prev != None:
             self.tail = self.f[key].prev
        
        elif self.f[key].prev == None and self.f[key].next != None:
            
             self.head = self.f[key].next
             self.head.prev = None
            
        
        else:
             self.head = self.tail = None
            
        self.f[key] = None

        
    def add(self,key,value):
        
        if not self.head:
            self.head = self.tail = doubleLinkedList(key,value)
        
        else:
            self.tail.next = doubleLinkedList(key,value,self.tail)
            self.tail = self.tail.next
        
        self.f[key] = self.tail
    
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)