class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        degree = defaultdict(list)
        q = deque()
        visited = set()
        answer = []
        for x,y in adjacentPairs:
            degree[x].append(y)
            degree[y].append(x)
            
        
        for key in degree.keys():
            if len(degree[key]) == 1:
                q.append(key)
                break
        
        while(q):
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            answer.append(node)
            for n in degree[node]:
                q.append(n)
        
        return answer
            
            
            