class MyCircularQueue:

    def __init__(self, k: int):
        self.q = deque()        
        self.limit = k
    def enQueue(self, value: int) -> bool:
        
        if len(self.q) == self.limit:
            return False
        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        if len(self.q) > 0:
            self.q.popleft()
            return True
        return False

    def Front(self) -> int:
        if len(self.q) > 0:
            return self.q[0]
        
        return -1

    def Rear(self) -> int:
        if len(self.q) > 0:
            return self.q[-1]
        
        return -1

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()