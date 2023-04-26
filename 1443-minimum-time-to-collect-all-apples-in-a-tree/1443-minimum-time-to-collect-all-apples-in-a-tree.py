class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        self.time = 0
        def dfs(node,parent):
            apple = False
            
            for child in graph[node]:
                if child != parent:
                    check = dfs(child,node)
                    if check:
                        self.time += 2
                    apple = check or apple
                    
            
            
            return hasApple[node] or apple
        
        dfs(0,-1)
        return self.time