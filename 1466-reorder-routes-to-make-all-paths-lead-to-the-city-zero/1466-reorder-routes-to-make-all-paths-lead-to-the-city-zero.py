class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        queue = deque([(0,0)])
        edges_changed = 0
        visited = set()
        
        graph = defaultdict(list)
        
        for u,v in connections:
            
            graph[u].append([v,1])
            graph[v].append([u,0])
        
        while(queue):
            
            node,value = queue.popleft()
            
            if node in visited:
                continue
            visited.add(node)
            edges_changed += value
            
            for neigbour,val in graph[node]:
                
                queue.append((neigbour,val))
            
        return edges_changed
            