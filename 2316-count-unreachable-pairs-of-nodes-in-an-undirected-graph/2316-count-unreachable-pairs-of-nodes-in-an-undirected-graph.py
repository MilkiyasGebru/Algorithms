class Solution:
    
    def countNodes(self,node,graph,visited):
        
        if node in visited:
            return 0
        
        visited.add(node)
        total = 1
        
        for neigbour in graph[node]:
            total += self.countNodes(neigbour,graph,visited)
            
        return total
    
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        visited = set()
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        total_pairs = 0
        for i in range(n):
            if i not in visited:
                nodes = self.countNodes(i,graph,visited)
                total_pairs += nodes*(n-nodes)
                
        return total_pairs//2