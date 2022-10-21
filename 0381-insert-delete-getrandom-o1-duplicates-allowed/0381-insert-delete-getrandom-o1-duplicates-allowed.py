class RandomizedCollection:

    def __init__(self):
        
        self.numbers = []
        self.position = defaultdict(set)

    def insert(self, val: int) -> bool:
        
        isNotFound = len(self.position[val]) == 0
        self.numbers.append(val)
        self.position[val].add(len(self.numbers)-1)
        
        return isNotFound
        

    def remove(self, val: int) -> bool:
        
        isFound = len(self.position[val]) > 0
        
        if isFound :
            
            for index in self.position[val]:
                break
                
            self.position[val].remove(index)
            self.numbers[-1],self.numbers[index]=self.numbers[index],self.numbers[-1]
            self.numbers.pop()
            
            if index < len(self.numbers):
                
                self.position[self.numbers[index]].remove(len(self.numbers))
                self.position[self.numbers[index]].add(index)
                
            return True
            
        return False

    def getRandom(self) -> int:
        
        return random.choice(self.numbers)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()