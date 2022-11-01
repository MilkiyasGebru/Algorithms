class Solution:
    def check(self,row,col,n,m):
        
        return 0 <= row < n and 0 <= col < m
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        falls_array = []
        
        for col in range(len(grid[0])):
            falls_array.append([0,col])
        
        for row in range(len(grid)):

            for col in range(len(grid[0])):
                
                if falls_array[col] == False:
                    continue
                    
                r = falls_array[col][0]
                c = falls_array[col][1]
                
                if self.check(r,c+ grid[r][c],len(grid),len(grid[0])) and grid[r][c] == grid[r][c + grid[r][c]]:
                    falls_array[col] = [r+1,c+grid[r][c]]
                    
                else:
                    
                    falls_array[col]=False
                
        answer = []
        
        for col in range(len(falls_array)):
            
            if falls_array[col]!=False:
                
                answer.append(falls_array[col][1])
                
            else:
                
                answer.append(-1)
                
        return answer
                    
                