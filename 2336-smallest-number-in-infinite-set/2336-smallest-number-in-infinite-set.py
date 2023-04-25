class SmallestInfiniteSet:

    def __init__(self):
        
        self.heap = []
        self.currNum = 1
        self.visited = set()
        
    def popSmallest(self) -> int:
        
        if len(self.heap) == 0 or self.currNum < self.heap[0]:
            num = self.currNum
            self.currNum += 1
            while self.currNum in self.visited:
                self.currNum += 1
            
            
        else:
            
            num = heapq.heappop(self.heap)
            self.visited.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if num not in self.visited and num != self.currNum:
            heapq.heappush(self.heap,num)
            self.visited.add(num)
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)