class Solution:
    
    def detontate(self,graph,bomb):
        
        visited = set()
        q = deque([bomb])
        detonated_bombs = 0
        
        while(q):
            
            node = q.popleft()
            if node in visited:
                continue
                
            visited.add(node)
            
            detonated_bombs += 1
            
            for neigbour in graph[node]:
                q.append(neigbour)
        
        return detonated_bombs
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        max_bomb = 1
        
        for i in range(len(bombs)):
            
            for j in range(len(bombs)):
                
                if i == j:
                    continue
                
                if ((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2) <= bombs[i][2] ** 2:
                    
                    graph[i].append(j)

        
        for i in range(len(bombs)):
            max_bomb = max(max_bomb, self.detontate(graph,i))
        
        return max_bomb
                
                
            
                