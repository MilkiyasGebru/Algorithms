class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        q = deque()
        adj = defaultdict(list)
        max_size = max(src,dst)
        for inital,dist,price in flights:
            max_size = max(inital,dist,max_size)
            adj[inital].append([dist,price])
        distance = [inf for _ in range(max_size+1)]
        
        q.append((src,0))
        while(q and k+1 > -1):
            size = len(q)
            for _ in range(size):
                node,dis = q.popleft()
                if distance[node] <= dis:
                    continue
                distance[node]=dis
                for n,price in adj[node]:
                    q.append((n,dis+price))
            k-=1
        return distance[dst] if distance[dst] != inf else -1
                
    