class SeatManager:

    def __init__(self, n: int):
        
        self.small = 1
        self.heap = []
        
    def reserve(self) -> int:
        
        if self.heap and self.heap[0] < self.small:
            return heappop(self.heap)
        self.small += 1
        return self.small - 1

    def unreserve(self, seatNumber: int) -> None:
        
        heappush(self.heap,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)