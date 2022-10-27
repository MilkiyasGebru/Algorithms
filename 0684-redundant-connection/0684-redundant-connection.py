class UnionFind:
    
    def __init__(self,n):
        self.size = [0 for _ in range(n)]
        self.parent = [i for i in range(n)]
    
    def find(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,u,v):
        
        parent_u = self.find(u)
        parent_v = self.find(v)
        
        if parent_u == parent_v:
            return True
        
        if self.size[parent_u] > self.size[parent_v]:
            
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
        else:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        return False
        
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        component = UnionFind(len(edges))
        cycle = []
        for u,v in edges:
            isCycle = component.union(u-1,v-1)
            if isCycle:
                cycle=[u,v]
        return cycle