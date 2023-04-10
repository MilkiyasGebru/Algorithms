class Solution:
        
    def findMax(self,f,g):
        
        for i in range(26):
            f[i] = max(f[i],g[i])
        
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
    
        
        visited = [0 for i in range(len(colors))]
        graph = defaultdict(list)
        answer = 0
        
        for u,v in edges:
            
            graph[u].append(v)
        
        @lru_cache(None)
        def dfs(node):
            
            if visited[node] == 1:
                return defaultdict(lambda : inf)
            
            if visited[node] == 2:
                return f[node]
            
            f = defaultdict(int)
            visited[node] = 1
            
            for child in graph[node]:
                
                self.findMax(f,dfs(child))
                
            visited[node] = 2
                
                
            f[ord(colors[node])-ord("a")] += 1
            return f
        
        for i in range(len(colors)):
            if visited[i] == 0:
                answer = max(max(dfs(i).values()),answer)
                if answer == inf:
                    return -1
        
        return answer 
            
        
        
