class Solution:
    
    def findCycleSize(self,node,edges,in_degree):
        
        if in_degree[node] == 0:
            return 0
        
        in_degree[node] -= 1
        
        return 1 + self.findCycleSize(edges[node],edges,in_degree)
    
    def longestCycle(self, edges: List[int]) -> int:
        
        in_degree = [0 for _ in range(len(edges))]
        queue = deque()
        
        for i in range(len(edges)):
            
            if edges[i] != -1:
                in_degree[edges[i]] += 1
                
        for i in range(len(edges)):
            if in_degree[i] == 0:
                queue.append(i)
                
        while queue:
            
            node = queue.popleft()
            
            if edges[node] != -1:
                in_degree[edges[node]] -= 1
                
            if edges[node] != - 1 and in_degree[edges[node]] == 0:
                queue.append(edges[node])
                
        max_cycle = -1
        
        for i in range(len(edges)):
            
            if in_degree[i] != 0:
                max_cycle = max(max_cycle,self.findCycleSize(i,edges,in_degree))
        
        return max_cycle
        