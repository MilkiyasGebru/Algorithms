class Solution:
    
    
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        elements = {}
        
        for row in range(len(matrix)):
            
            for col in range(len(matrix[0])):
                
                if (row-col) not in elements:
                    elements[row-col]=matrix[row][col]
                elif matrix[row][col]!=elements[row-col]:
                    return False
        return True