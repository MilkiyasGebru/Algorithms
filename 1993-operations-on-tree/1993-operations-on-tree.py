class LockingTree:

    def __init__(self, parent: List[int]):
        
        self.parent = parent
        self.graph = defaultdict(list)
        for node in range(1,len(parent)):
            self.graph[parent[node]].append(node)
        self.f = {}
            

    def lock(self, num: int, user: int) -> bool:
        
        if num not in self.f:
            self.f[num] = user
            return True
        

    def unlock(self, num: int, user: int) -> bool:
        
        if num in self.f and self.f[num] == user:
            del self.f[num]
            return True
        
    def upgrade(self, num: int, user: int) -> bool:
        
        if self.upward(num) and self.downWard(num):
            self.f[num] = user
            return True
        
    def upward(self,num:int)-> bool:
        
        if num == -1:
            return True
        
        if num not in self.f:
            return self.upward(self.parent[num])
        
    def downWard(self,num:int) -> bool:
        anyLocked = False
        if num in self.f:
            anyLocked = True
            del self.f[num]
        for child in self.graph[num]:
            anyLocked = self.downWard(child) or anyLocked
        
        return anyLocked
                

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)