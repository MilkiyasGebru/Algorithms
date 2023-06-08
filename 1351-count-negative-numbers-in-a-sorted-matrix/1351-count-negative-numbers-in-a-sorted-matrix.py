class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        
        answer=0
        end = len(grid[0])-1
        
        for row in range(len(grid)):
            
            left = 0
            right = end
            index = end+1
            
            while(left<=right):
                
                mid = (left+right)//2
                if grid[row][mid] < 0:
                    right = mid - 1
                    
                    index = mid 
                else:
                    
                    left = mid + 1
                    
            if end - index >=0:
                
                answer += (end-index+1)*(len(grid)-(row))
                # print(answer)
                end = index - 1
             
                
        return answer    