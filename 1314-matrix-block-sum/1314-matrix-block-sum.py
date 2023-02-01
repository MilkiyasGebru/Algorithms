class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        row_length = len(mat) - 1
        col_length = len(mat[0]) - 1
        
        def valid(row,col):
            
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                return mat[row][col]
            return 0
        for row in range(len(mat)):
            
            for col in range(len(mat[0])):
                
                mat[row][col] += valid(row-1,col) + valid(row,col-1) - valid(row-1,col-1)
        
        
        answer = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        for row in range(len(mat)):
            
            for col in range(len(mat[0])):
                
                answer[row][col] = valid( min( row_length, row+k ),min( col_length, col + k) ) - valid( min( row_length, row+k ),col-k-1 ) - valid( row-k-1 , min( col_length, col + k)) + valid( row - k -1, col - k - 1) 
        
        return answer