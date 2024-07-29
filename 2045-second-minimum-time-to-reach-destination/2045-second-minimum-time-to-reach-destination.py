class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        
        
        graph = defaultdict(list)
        f = defaultdict(set)
        
        inital_time = 0
        heap = [(inital_time,1)]
        
        for u,v in edges:    
            
            graph[u].append(v)
            graph[v].append(u)
        
        while heap:
            
            cur_time,node = heapq.heappop(heap)
            
            if len(f[node]) >= 2:
                continue

            f[node].add(cur_time)
            
            for neigb in graph[node]:
                
                val = cur_time // change
                rem = cur_time % change
                
                if val%2 != 0:
                    cur_time += change - rem
                    
                heapq.heappush(heap,( cur_time + time ,neigb))
        return max(f[n])
        
    
        