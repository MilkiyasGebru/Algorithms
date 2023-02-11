class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph= {}
        q=deque([(0,-1),(0,1)])
        
        blueGraph = defaultdict(list)
        redGraph = defaultdict(list)
        
        graph[1]=blueGraph
        graph[-1]=redGraph
        
        visited = set()
        
        for a,b in blueEdges:
            blueGraph[a].append(b)
            
        for a,b in redEdges:
            redGraph[a].append(b)
        
        shortestPath = [math.inf for i in range(n)]
        
        path = 0
        while(q):
            size = len(q)
            for _ in range(size):
                node,preColor = q.popleft()
                if (node,preColor) in visited:
                    continue
                visited.add((node,preColor))
                shortestPath[node] = min(shortestPath[node],path)
                
                for n in graph[preColor*-1][node]:
                    q.append((n,preColor*-1))
        
            path += 1
        for i in range(len(shortestPath)):
            
            if shortestPath[i] == math.inf:
                shortestPath[i] = -1

        return shortestPath
                
        
        
            
        
        
        