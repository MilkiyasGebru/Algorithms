class Solution:
    
    def maxCycle(self,node,edges,indegree):
        
        cycle = 0
        while(indegree[node] > 0):
            
            cycle += 1
            indegree[node] -= 1
            node = edges[node]
            
        return cycle
        
    
    def longestCycle(self, edges: List[int]) -> int:
        
        indegree = [0 for _ in range(len(edges))]
        answer = - 1
        q = deque()
        
        for i in range(len(edges)):
            if edges[i] != -1:
                indegree[edges[i]] += 1
        
        for i in range(len(edges)):
            if indegree[i] == 0:
                q.append(i)
                
        while(q):
            
            node = q.popleft()
            if edges[node] != -1:
                indegree[edges[node]] -= 1
            if edges[node] != -1 and indegree[edges[node]] == 0:
                q.append(edges[node])
                
        for i in range(len(edges)):
            if indegree[i] != 0:
                answer = max(answer,self.maxCycle(i,edges,indegree))
        
        return answer