class SmallestInfiniteSet:

    def __init__(self):
        self.num = 1
        self.heap = []
        self.visited = set()
        
    def popSmallest(self) -> int:
        if self.heap and self.heap[0] < self.num:
            self.visited.add(self.heap[0])
            return heappop(self.heap)
        self.visited.add(self.num)
        self.num += 1
        return self.num - 1

    def addBack(self, num: int) -> None:
        
        if num  in self.visited:
            self.visited.remove(num)
            heappush(self.heap,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)