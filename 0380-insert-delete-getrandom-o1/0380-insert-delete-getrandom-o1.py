class RandomizedSet:

    def __init__(self):

        self.f = {}  
        self.length = 0
        self.index = 0
        
    def insert(self, val: int) -> bool:
        
        x = val not in self.f
        self.f[val]=1
        self.length += 1 if x else 0
        return x

    def remove(self, val: int) -> bool:
        
        x = val in self.f
        if x:
            del self.f[val]
        self.length -=1 if x else 0
        return x
        

    def getRandom(self) -> int:
        
        self.index = random.randint(0,self.length-1)
        keys = list(self.f.keys())
        val = keys[self.index]
        self.index += 1
        return val
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()