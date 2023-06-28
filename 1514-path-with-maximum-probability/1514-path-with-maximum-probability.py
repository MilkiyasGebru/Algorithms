class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        heap = [[-1,start]]
        visited = set()
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1],succProb[i]])
            graph[edges[i][1]].append([edges[i][0],succProb[i]])
        
        while heap :
            weight,node = heappop(heap)
            if node in visited:
                continue
            if node == end:
                return -1*weight
            visited.add(node)
            for neighbour,w in graph[node]:
                heappush(heap,(-1*abs(w*weight),neighbour))
        
        return 0
            