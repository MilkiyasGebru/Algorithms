class UnionFind:
    def __init__(self,points):
        self.parent = [i for i in range(len(points))]
        self.rank  = [0 for _ in range(len(points))]
        self.components = len(points)
    def union(self,par1,par2):
        par1 = self.findParent(par1)
        par2 = self.findParent(par2)
        if par1 == par2:
            return
        self.components -=1
        if self.rank[par2] > self.rank[par1]:
            par1,par2 = par2,par1
        self.parent[par2] = par1
        self.rank[par1] += self.rank[par2]
    def findParent(self,par):
        if self.parent[par] == par:
            return par
        self.parent[par] = self.findParent(self.parent[par])
        return self.parent[par]
    def remaining_stones(self):
        return self.components
    

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Basically the number of components
        graph = UnionFind(stones)
        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph.union(i,j)
        
        
        return len(stones) - graph.remaining_stones()