class RandomizedSet:

    def __init__(self):
        
        self.position = defaultdict(set)
        self.numbers = []

    def insert(self, val: int) -> bool:
        
        if len(self.position[val]) > 0:
            return False
        
        self.position[val].add(len(self.numbers))
        self.numbers.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        
        if len(self.position[val]) == 0:
            return False
        
        index = self.position[val].pop()
        self.numbers[index],self.numbers[-1] = self.numbers[-1],self.numbers[index]
        self.numbers.pop()
        
        if index < len(self.numbers):
            
            self.position[self.numbers[index]].remove(len(self.numbers))
            self.position[self.numbers[index]].add(index)
        
        return True

    def getRandom(self) -> int:
        
        return random.choice(self.numbers)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()