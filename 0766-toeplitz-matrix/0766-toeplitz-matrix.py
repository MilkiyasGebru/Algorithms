class Solution:
    
    def isValid(self,row,col,m,n):
        
        return 0 <= row < m and 0 <= col < n
    
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        
        for row in range(1,len(matrix)):
            
            for col in range(1,len(matrix[0])):
                
                if self.isValid(row-1,col-1,len(matrix),len(matrix[0])) and matrix[row][col]!=matrix[row-1][col-1]:
                    return False
                
        return True