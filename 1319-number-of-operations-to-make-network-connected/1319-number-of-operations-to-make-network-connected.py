class UnionFind:
    
    def __init__(self,n):
        
        self.parent = [ i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def findParent(self,computer):
        
        if self.parent[computer] == computer:
            return computer
        
        self.parent[computer] = self.findParent(self.parent[computer])
        return self.parent[computer]
    
    def union(self,u,v):
        
        parent1 = self.findParent(u)
        parent2 = self.findParent(v)
        
        if parent1 == parent2:
            return 1
        
        if self.rank[parent1] > self.rank[parent2]:
            
            self.parent[parent2] = parent1
            self.rank[parent2] += self.rank[parent1]
            
        elif self.rank[parent1] < self.rank[parent2]:
            
            self.parent[parent1] = parent2
            self.rank[parent1] += self.rank[parent2]
        
        else:
            self.parent[parent1] = parent2
            self.rank[parent1] += 1
        
        return 0
    def total_parents(self):
        parents = set()
        for i in range(len(self.parent)):
            parents.add(self.findParent(self.parent[i]))
        
        return len(parents)-1
        

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        redudant_cabels = 0
        network = UnionFind(n)
        for u,v in connections:
            redudant_cabels += network.union(u,v)
        
        cabels_needed = network.total_parents()
        
        return -1 if cabels_needed > redudant_cabels else cabels_needed
        
        
        
        
        