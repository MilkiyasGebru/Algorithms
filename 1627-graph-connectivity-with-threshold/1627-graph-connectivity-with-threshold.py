class UnionFind:
    
    def __init__(self,n):
        self.rank = [0 for _ in range(n)]
        self.parent = [i for i in range(n)]
    
    def findParent(self,n):
        if n == self.parent[n]:
            return n
        self.parent[n] = self.findParent(self.parent[n])
        return self.parent[n]
    
    def union(self,u,v):
        par1 = self.findParent(u)
        par2 = self.findParent(v)
        
        if par1 == par2:
            return
        if self.rank[par2] > self.rank[par1]:
            par1,par2 = par2,par1
        self.rank[par1]+=self.rank[par2]
        self.parent[par2]=par1

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        graph = UnionFind(n+1)
        for factor in range(threshold+1,n+1):
            i = 1
            num = factor
            while num <= n:
                
                graph.union(num,factor)
                i += 1
                num = i*factor
        answer = []
        for u,v in queries:
            answer.append(graph.findParent(u) == graph.findParent(v))
        
        return answer
                
            
            
            
        