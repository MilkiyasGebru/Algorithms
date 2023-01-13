class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]
    def check(self,n):
        return self.find(n) == self.find(1)
    
    def find(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self,a,b):
        par1 = self.find(a)
        par2 = self.find(b)
        if par1 == par2:
            return
        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
        elif self.rank[par2] > self.rank[par1]:
            self.parent[par1] = par2
        else:
            self.rank[par1] += 1
            self.parent[par2] = par1
           
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        path = UnionFind(n)
        
        for u,v, dist in roads:
            path.union(u,v)
        answer = math.inf
        
        for u,v,dist in roads:
            if path.check(u):
                answer = min(answer,dist)
        return answer
        