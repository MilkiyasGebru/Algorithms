class Solution:
    
    def calculate_submatrix(self,array):
        submatrix = 0
        array.sort()
        for i in range(len(array)-1,-1,-1):
            submatrix = max(submatrix,array[i]*(len(array)-i))
        return submatrix
    
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        heights = defaultdict(list)
        
        for col in range(len(matrix[0])):
            last_zero = -1
            for row in range(len(matrix)):
                if matrix[row][col] == 0:
                    last_zero = row
                heights[row].append(row-last_zero)
        largest_submatrix = 0
        for row in range(len(matrix)):
            largest_submatrix = max(largest_submatrix,self.calculate_submatrix(heights[row]))
        
        return largest_submatrix