class Solution:
    
    def dfs(self,node,graph,visited):
        
        if node in visited:
            return 
        
        visited.add(node)
        
        for neigbour in graph[node]:
            self.dfs(neigbour,graph,visited)
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n - 1:
            return -1
        
        visited = set()
        graph = defaultdict(list)
        components = 0
        
        for u,v in connections:
            
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(n):
            
            if i not in visited:
                
                components += 1
                self.dfs(i,graph,visited)
        
        return components - 1
        
        
        
        
        
        