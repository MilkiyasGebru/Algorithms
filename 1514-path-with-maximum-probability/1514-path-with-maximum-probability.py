# from collections import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            
            graph[edges[i][0]].append((succProb[i],edges[i][1]))
            graph[edges[i][1]].append((succProb[i],edges[i][0]))
        
        heap = []
        heapq.heappush(heap,(-1,start_node))
        visited = set()
        
        while heap:
            
            weight,node = heapq.heappop(heap)
            
            if node in visited:
                continue
                
            if node == end_node:
                return -1*weight
                
            visited.add(node)
            for wx,neigbour in graph[node]:
                heapq.heappush(heap,(wx*weight, neigbour))
        
        return 0
            