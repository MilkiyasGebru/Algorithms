class UnionFind:
    
    def __init__(self,n):
        
        self.size = [1 for i in range(n)]
        self.parent = [i for i in range(n)]
    
    def findParent(self,node):
        
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        
        return self.parent[node]
    def union(self,node1,node2):
        
        par1 = self.findParent(node1)
        par2 = self.findParent(node2)
        
        if par1 == par2:
            return
        
        if self.size[par1] > self.size[par2]:
            self.parent[par2] = self.parent[par1]
            self.size[par1] += self.size[par2]
        else:
            self.size[par2] += self.size[par1]
            self.parent[par1] = self.parent[par2]
        
            

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        secret = UnionFind(n)
        graph = defaultdict(list)
        secret.union(0,firstPerson)
        
        for i in range(len(meetings)):
            
            graph[meetings[i][2]].append((meetings[i][0],meetings[i][1]))
            
        for key in sorted(graph.keys()):
            
            for u,v in graph[key]:
                secret.union(u,v)
                
            for u,v in graph[key]:
                
                if secret.findParent(u) != secret.findParent(0):
                    
                    
                    secret.parent[u] = u
                    secret.parent[v] = v
                    secret.size[u] =secret.size[v] = 1 
            
        return [i for i in range(n) if secret.findParent(i) == secret.findParent(0)]
            
        