class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q=deque()
        visited = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def isValid(row,col):
            
            return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col]=="."
        
        def isEnd(row,col):
            return (0 == col or col == len(maze[0])-1 or row == 0 or row == len(maze)-1) and (row,col) != tuple(entrance)
        q.append((entrance[0],entrance[1]))
        ans = 0
        while(q):
            x = len(q)
            for _ in range(x):
                r,c = q.popleft()
                if (r,c) in visited:
                     continue
                visited.add((r,c))
                if isEnd(r,c):
                    
                    return ans
                for i,j in directions:
                    if isValid(i+r,c+j):
                        q.append((r+i,c+j))
            ans+=1
        return -1
                
                