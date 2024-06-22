class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        
        new_edges = defaultdict(list)
        for u,v in edges:
            new_edges[u].append(v)
            new_edges[v].append(u)
        visited = set()
        queue = deque([0])
        graph = defaultdict(list)
        
        while queue:
            
            node = queue.popleft()
            
            if node in visited:
                continue
            visited.add(node)
            for neigb in new_edges[node]:
                if neigb not in visited:
                    graph[node].append(neigb)
                    queue.append(neigb)
        for node in range(len(values)):
            if len(graph[node]) == 0:
                graph[node].append(None)
        @cache
        def dp(node,boolean):
            if node == None:
                return 0 if boolean else -math.inf
            
            path1 = 0
            
            for neigb in graph[node]:
                
                path1 += dp(neigb,True)
            
            path2 = values[node]
            
            for neigb in graph[node]:
                path2 += dp(neigb,boolean)
            
            return max(path1,path2)
        
        return dp(0,False)