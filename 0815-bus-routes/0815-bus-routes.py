class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        new_routes = [ set(routes[i]) for i in range(len(routes))]
        
        visited_set = set()
        
        q = deque([source])
        shortest_path = 0
        while(q):
            
            size = len(q)
            for _ in range(size):
                
                node = q.popleft()
                if node in visited_set:
                    continue
                
                visited_set.add(node)
                if node == target:
                    return shortest_path
                
                for i in range(len(new_routes)):
                    
                    if node in new_routes[i]:
                        
                        for x in new_routes[i]:
                            q.append(x)
                        new_routes[i] = set()
            shortest_path += 1
        
        
        
        
        
        return -1