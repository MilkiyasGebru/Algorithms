class Solution:
    
    def dijkstra(self,source_node,graph,f):
        visited = set()
        heap = [(0,source_node)]
        
        while heap:
            val,node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            f[source_node+node] = val
            for neigb_node,neigb_val in graph[node]:
                heapq.heappush(heap,(neigb_val + val,neigb_node))
            
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        graph = defaultdict(list)
        f = defaultdict(lambda:math.inf)
        for i in range(len(original)):
            graph[original[i]].append([changed[i],cost[i]])
        for i in range(26):
            self.dijkstra(chr(ord("a")+i),graph,f)
        min_cost = 0
        for i in range(len(source)):
            min_cost += f[source[i]+target[i]]
        return min_cost if min_cost != math.inf else -1