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
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        graph = UnionFind(n)
        answer = []
        for u,v in requests:
            par1,par2 = graph.findParent(u),graph.findParent(v)
            canNotUnion = False
            for a,b in restrictions:
                par3,par4 = graph.findParent(a), graph.findParent(b)
                canNotUnion = canNotUnion or (par3 in [par1,par2] and par4 in [par1,par2])
            answer.append(not canNotUnion)
            if not canNotUnion:
                graph.union(u,v)
        return answer
            