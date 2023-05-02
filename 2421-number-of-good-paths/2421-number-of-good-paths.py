class UnionFind:
    def __init__(self,n):
        self.f =defaultdict(lambda:defaultdict(int))
        self.parent = [i for i in range(n)]
        self.rank =   [1 for _ in range(n)]
    
    def findParent(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def unionNode(self,node1,node2,value):
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if parent1 == parent2:
            return 0
        if self.rank[parent2] > self.rank[parent1]:
            parent2,parent1=parent1,parent2
        
        self.rank[parent1] += self.rank[parent2]
        self.parent[parent2] = parent1
        ans = self.f[parent1][value]*self.f[parent2][value]
        self.f[parent1][value] += self.f[parent2][value]
        return ans
    
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        answer = len(vals)
        graph = UnionFind(len(vals))
        
        for i in range(len(edges)):
            edges[i].append(max(vals[edges[i][0]],vals[edges[i][1]]))
            
        for i in range(len(vals)):
            graph.f[i][vals[i]] = 1
            
        edges.sort(key = lambda x : x[2])
        
        for u,v,val in edges:
            answer += graph.unionNode(u,v,val)
        return answer
        
        