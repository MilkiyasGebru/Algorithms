class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        color = [None for _ in range(n)]
        
        for u,v in dislikes:
            
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(node):
            
            q=deque([node])
            color[node-1] = 1
            while(q):
                
                node = q.popleft()
                                
                for child in graph[node]:
                    
                    if color[child-1] == color[node-1]:
                        return False
                    
                    if color[child-1] == None:
                        
                        color[child-1] = -1*color[node-1]
                        q.append(child)
                        
            return True
        
        for i in range(1,n+1):
            
            if color[i-1] == None:
                
                if not bfs(i):
                    
                    return False
        return True
                
        
            