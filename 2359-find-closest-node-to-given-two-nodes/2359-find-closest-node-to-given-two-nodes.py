class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        n = len(edges)
        visited = set()
        
        arr = [0]*n
        arr2 = [-inf]*n 
        
        q=deque()
        
        q.append((node1,0,0))
        q.append((node2,1,0))
        
        ans = [inf,0]
        
        while(q):
            
            node,prev,dis=q.popleft()
            
            if (node,prev) in visited:
                    
                continue
            
            visited.add((node,prev))
            arr[node]+=1
            arr2[node]=max(dis,arr2[node])
            
            if arr[node]==2:
                
                if ans[0] > arr2[node] or (ans[0]== arr2[node] and node < ans[1]):
                    ans = [arr2[node],node]
                    
            if edges[node]!=-1:
                q.append((edges[node],prev,dis+1))
        
        
        return ans[1] if ans[0]!= inf else -1
            