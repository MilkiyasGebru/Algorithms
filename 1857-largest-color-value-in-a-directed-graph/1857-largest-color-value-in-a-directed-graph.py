class Solution:
        
    def findMax(self,f,g):
        
        for i in range(26):
            f[i] = max(f[i],g[i])
        
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
    
        global_dict = {}
        visited = [0 for i in range(len(colors))]
        graph = defaultdict(list)
        answer = 0
        
        for u,v in edges:
            
            graph[u].append(v)
        
        def dfs(node):
            
            if visited[node] == 1:
                return math.inf
            
            if visited[node] == 2:
                return global_dict[node][ord(colors[node])-ord("a")]
            
            global_dict[node] = defaultdict(int)
            visited[node] = 1
            
            for child in graph[node]:
                
                if dfs(child) == math.inf:
                    return math.inf
                
                self.findMax(global_dict[node],global_dict[child])
                
            visited[node] = 2
            global_dict[node][ord(colors[node])-ord("a")] += 1
            
            return global_dict[node][ord(colors[node])-ord("a")]
        
        
        for i in range(len(colors)):
            
            answer = max(dfs(i),answer)
            
        
        return answer if answer != math.inf else -1
            
        
        
