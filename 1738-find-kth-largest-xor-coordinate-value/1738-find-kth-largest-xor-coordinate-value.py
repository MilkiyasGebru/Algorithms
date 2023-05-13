class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        n,m = len(matrix),len(matrix[0])
        
        directions = [(-1,0),(0,-1),(-1,-1)]
        def isInside(row,col):
            
            if 0 <= row < n and 0 <= col < m:
                return matrix[row][col]
            return 0
        
        heap = []
        
        for row in range(n):
            for col in range(m):
                
                for rx,cx in directions:
                    matrix[row][col] ^= isInside(row+rx,col + cx)
                    
                heappush(heap, matrix[row][col])
                
                if len(heap) > k:
                    heappop(heap)
                    
        return heappop(heap)