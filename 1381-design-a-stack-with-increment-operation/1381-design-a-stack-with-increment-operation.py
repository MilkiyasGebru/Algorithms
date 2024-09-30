class CustomStack:

    def __init__(self, maxSize: int):
        self.array = []    
        self.maxSize = maxSize
    def push(self, x: int) -> None:
        if len(self.array) < self.maxSize:
            self.array.append(x)

    def pop(self) -> int:
        if len(self.array) == 0:
            return -1
        return self.array.pop()
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.array))):
            self.array[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)