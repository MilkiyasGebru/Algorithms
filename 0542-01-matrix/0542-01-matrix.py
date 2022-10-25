class Solution:
    def isValid(self, row ,col ,m,n):
        
        return 0 <= row < m and 0 <= col < n 
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        answer = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        queue = deque()
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]==0:
                    queue.append((row,col))
        move = 0
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while(queue):
            size = len(queue)
            for _ in range(size):
                row,col = queue.popleft()
                if mat[row][col]=="#":
                    continue
                mat[row][col]="#"
                answer[row][col] = move

                for i,j in directions:
                    if self.isValid(row+i,col+j,len(mat),len(mat[0])) and mat[row+i][col+j] == 1:
                        queue.append((row+i,col+j))
            move += 1
        return answer
            
                    
            
        
        