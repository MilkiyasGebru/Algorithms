class Solution:
    def isValid(self,row,col,m,n):        
        return 0 <= row < m and 0 <= col < n
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        directions = [(0,1),(1,0)]
        for row in range(len(obstacleGrid)-1,-1,-1):
            for col in range(len(obstacleGrid[0])-1,-1,-1):
            
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col]=0
                    continue
                    
                elif (row,col) == (len(obstacleGrid)-1,len(obstacleGrid[0])-1):
                    obstacleGrid[row][col]=1
                else:
                    for i,j in directions:
                        if self.isValid(row+i,col+j,len(obstacleGrid),len(obstacleGrid[0])):
                            obstacleGrid[row][col] += obstacleGrid[row+i][col+j]
        return obstacleGrid[0][0]
                
        
        