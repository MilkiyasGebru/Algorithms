class Solution:
    
    def buildGraph(self,k,rowConditions):
        
        rowGraph = defaultdict(set)
        rowDegree = [0 for _ in range(k+1)]
        
        for u,v in rowConditions:
            rowGraph[u].add(v)
        
        queue = deque()
        for i in range(1,k+1):
            for child in rowGraph[i]:
                rowDegree[child] += 1
        for i in range(1,k+1):
            if rowDegree[i] == 0:
                queue.append(i)
        assigned_row = 0
        rows = {}
        while queue:
            node = queue.popleft()
            rows[node] = assigned_row
            assigned_row += 1
            
            for child in rowGraph[node]:
                
                rowDegree[child] -= 1
                if rowDegree[child] == 0:
                    queue.append(child)

        if assigned_row != k:
            return {}
        return rows
    
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        rows = self.buildGraph(k, rowConditions)
        cols = self.buildGraph(k, colConditions)
        
        if rows == {} or cols == {}:
            return []
        
        matrix = [[0 for _ in range(k)] for _ in range(k)]
        
        for i in range(1,k+1):
            matrix[rows[i]][cols[i]] = i
        
        return matrix
            