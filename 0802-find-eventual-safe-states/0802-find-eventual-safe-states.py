class Solution:
    
    def topSort(self,node,graph,colors):
        
        if colors[node] == 2:
            return True
        
        if colors[node] == 1:
            return False
        
        colors[node] = 1
        
        for neigbour in graph[node]:
            if not self.topSort(neigbour,graph,colors):
                return False
        
        colors[node] = 2
        return True
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        safe_nodes = []
        colors = [0 for _ in range(len(graph))]
        
        for i in range(len(graph)):
            
            if self.topSort(i,graph,colors):
                safe_nodes.append(i)
        
        return safe_nodes
        
        