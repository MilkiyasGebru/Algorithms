class UnionFind:
    
    def __init__(self,n):
        
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def findParent(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def unionNode(self,node1,node2):
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        
        if parent1 == parent2:
            return 1
        
        if self.rank[parent2] > self.rank[parent1]:
            parent1,parent2 = parent2,parent1
        
        self.rank[parent1] += self.rank[parent2]
        self.parent[parent2] = parent1
        return 0
    def check(self):
        boolean = True
        for i in range(len(self.parent)):
            boolean = boolean and self.findParent(i) == self.findParent(0)
        return boolean

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        alice = UnionFind(n)
        bob = UnionFind(n)
        extra_edges = 0
        edges.sort(key = lambda x: x[0],reverse = True)
        
        for typ,v,u in edges:
            
            if typ == 1:
                extra_edges += alice.unionNode(u-1,v-1)
                
            elif typ == 2:
                extra_edges += bob.unionNode(u-1,v-1)
                
            else:
                extra_edges += alice.unionNode(u-1,v-1)*bob.unionNode(u-1,v-1)
                
        if alice.check() and bob.check():
            return extra_edges
        
        return -1
        
        
        