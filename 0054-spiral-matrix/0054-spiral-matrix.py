class Solution:
    
    def isValid(self, row, col,  matrix):
        
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col]!= "#"
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        direction = { 0 :(0,1), 1 : (1,0), 2: (0,-1), 3 : (-1,0) }
        
        return self.rec(0, 0, matrix, [], 0, direction)
    
    def rec(self,row,col,matrix,stack,arrow,direction):
        
        stack.append(matrix[row][col])
        matrix[row][col]="#"
        
        if len(stack) == len(matrix[0])*len(matrix):
            return stack
        
        if self.isValid(row + direction[arrow][0], col + direction[arrow][1], matrix):
            return self.rec(row + direction[arrow][0], col + direction[arrow][1], matrix, stack, arrow, direction)
        
        new_arrow = ( arrow + 1)%4
        
        return self.rec(row + direction[new_arrow][0], col + direction[new_arrow][1], matrix, stack, new_arrow, direction)
        
        
        