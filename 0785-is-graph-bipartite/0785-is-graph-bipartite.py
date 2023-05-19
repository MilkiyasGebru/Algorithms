class Solution:
    def color_graph(self,node,colors,graph):
        
        for child in graph[node]:
            
            if colors[node] == colors[child]:
                return False
            
            if colors[child] == -1 :
                colors[child] = 1 - colors[node]
                if not self.color_graph(child,colors,graph):
                    return False
                
        return True
                
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        colors = [-1 for _ in range(len(graph))]
        
        for i in range(len(graph)):
            
            if colors[i] == -1:
                colors[i] = 0
                if not self.color_graph(i,colors,graph):
                    return False
        
        return True