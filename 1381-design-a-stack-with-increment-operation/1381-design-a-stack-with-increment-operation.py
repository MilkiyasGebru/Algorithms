class CustomStack:

    def __init__(self, maxSize: int):
        self.array = []    
        self.k = []
        self.maxSize = maxSize
    def push(self, x: int) -> None:
        if len(self.array) < self.maxSize:
            self.array.append(x)
            self.k.append(0)

    def pop(self) -> int:
        if len(self.array) == 0:
            return -1
        
        if len(self.k) > 1:
            self.k[-2] += self.k[-1]
        return self.k.pop() + self.array.pop()
        

    def increment(self, k: int, val: int) -> None:
        max_k = min(k,len(self.array))
        if max_k > 0:
            self.k[max_k-1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)