class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        visited = set()
        arr = [0]*n
        arr2 = [-inf]*n
        
        graph = defaultdict(list)
        for i in range(len(edges)):
            if edges[i] != -1:
                graph[i].append(edges[i])
        q=deque()
        q.append((node1,0,0))
        q.append((node2,1,0))
        while(q):
            node,prev,dis=q.popleft()
            
            if (node,prev) in visited:
                    
                continue
            
            visited.add((node,prev))
            arr[node]+=1
            arr2[node]=max(dis,arr2[node])
            for c in graph[node]:
                q.append((c,prev,dis+1))
        ans = [inf,0]
        for i in range(len(arr2)):
            if arr2[i]==-inf or arr[i]!=2:
                continue
            if ans[0] > arr2[i]:
                ans = [arr2[i],i]
        return ans[1] if ans[0]!= inf else -1
            