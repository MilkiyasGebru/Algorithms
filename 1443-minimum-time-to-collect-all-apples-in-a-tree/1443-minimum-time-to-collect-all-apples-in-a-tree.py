class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node,parent):
            cost = 0
            
            for child in graph[node]:
                
                if child != parent:
                    child_cost = dfs(child,node)
                    
                    if child_cost or hasApple[child]:
                        cost += 2 + child_cost
            return cost
        
        return dfs(0,-1)
