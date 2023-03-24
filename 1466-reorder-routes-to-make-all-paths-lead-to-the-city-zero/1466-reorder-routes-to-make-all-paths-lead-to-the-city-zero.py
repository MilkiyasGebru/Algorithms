class Solution:
    
    def dfs(self,node,parent,graph):
        
        
        edges_changed = 0
        
        for neigbour,val in graph[node]:
            if neigbour != parent:
                edges_changed += val + self.dfs(neigbour,node,graph)
        
        return edges_changed
    
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        queue = deque([(0,0)])
        edges_changed = 0
        visited = set()
        
        graph = defaultdict(list)
        
        for u,v in connections:
            
            graph[u].append([v,1])
            graph[v].append([u,0])
        
        return self.dfs(0,-1,graph)
            