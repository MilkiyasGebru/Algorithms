class Solution:
    
    def detontate(self,graph,bomb):
        
        visited = set()
        q = deque([bomb])
        
        while(q):
            
            node = q.popleft()
            
            if node in visited:
                continue
                
            visited.add(node)
            
            for neigbour in graph[node]:
                q.append(neigbour)
        
        return len(visited)
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        max_bomb = 1
        
        for i in range(len(bombs)):
            
            for j in range(i+1,len(bombs)):
                
                if ((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2) <= bombs[i][2] ** 2:
                    
                    graph[i].append(j)
                
                if ((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2) <= bombs[j][2] ** 2:
                    
                    graph[j].append(i)
                
        
        for i in range(len(bombs)):
            max_bomb = max(max_bomb, self.detontate(graph,i))
        
        return max_bomb
                
                
            
                