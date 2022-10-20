class RandomizedSet:

    def __init__(self):

        self.f = defaultdict(lambda:inf) 
        self.arr = []
        
    def insert(self, val: int) -> bool:
        
        isNotFound = self.f[val] == inf
        if isNotFound:
            self.arr.append(val)
            self.f[val]=len(self.arr)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        
        if self.f[val] == inf:
            return False
        
        index = self.f[val]
        self.arr[-1],self.arr[index]=self.arr[index],self.arr[-1]
        self.arr.pop()
        
        if index < len(self.arr):
            self.f[self.arr[index]] = index
            
        self.f[val]=inf
        return True
        

    def getRandom(self) -> int:
        
        index = random.randint(0,len(self.arr)-1)
        
        return self.arr[index]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()