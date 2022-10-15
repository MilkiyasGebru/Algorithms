class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        size = n
        indegree = [0 for _ in range(n)]
        graph = defaultdict(list)
        q = deque()
        
        for u,v in edges:
            
            indegree[u]+=1
            indegree[v]+=1
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(n):
            
            if indegree[i] <= 1:
                q.append(i)
        
        while(q and n > 2):
            
            levelSize = len(q)
            
            for _ in range(levelSize):
                
                node = q.popleft()
                
                if indegree[node]==inf:
                    continue
                    
                indegree[node]=inf
                n-=1
                
                for neig in graph[node]:
                    
                    indegree[neig]-=1
                    
                    if indegree[neig]==1:
                        q.append(neig)
                        
        return [i for i in range(size) if indegree[i] != inf]
                
        