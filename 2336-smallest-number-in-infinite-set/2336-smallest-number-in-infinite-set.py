class SmallestInfiniteSet:

    def __init__(self):
        
        self.heap = []
        for i in range(1000):
            heapq.heappush(self.heap,i+1)
        self.visited = set()
        
    def popSmallest(self) -> int:
        
        num = heapq.heappop(self.heap)
        self.visited.add(num)
        return num

    def addBack(self, num: int) -> None:
        
        if num in self.visited:
            self.visited.remove(num)
            heapq.heappush(self.heap,num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)