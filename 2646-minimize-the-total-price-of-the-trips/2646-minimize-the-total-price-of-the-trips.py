class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        '''
        I need to calculate how many times a node is touched during the total trips
        '''
        all_paths = defaultdict(int)
        single_path = defaultdict(int)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def make_trip(node,path,parent,end):
            
            if node == end:
                for key in path.keys():
                    if path[key] != 0:
                        all_paths[key] += 1
                return
            
            for neigb in graph[node]:
                if neigb != parent:
                    path[neigb] += 1
                    make_trip(neigb,path,node,end)
                    path[neigb] -= 1
        for start,end in trips:
            single_path[start] += 1
            make_trip(start,single_path,-1,end)
            single_path[start] -= 1
            
        @cache
        def rec(node,parent,can_halve):
            
                
            halved = all_paths[node] * (price[node]//2)
            non_halved = all_paths[node] * price[node]

            for neigb in graph[node]:
                if neigb != parent:
                    halved += rec(neigb,node,False)
                    non_halved += rec(neigb,node,True)
            
            if can_halve:
                return min(halved, non_halved)
            return non_halved
      
        return min(rec(0,-1,True),rec(0,-1,False))