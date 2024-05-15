class Solution:
    
    def isValid(self,row,col,grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])
    
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        # Start 
        # It is more of Union Find question 
        values = defaultdict(int)
        queue = deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1:
                    queue.append((row,col))
        visited = set()
        level = 0
        while queue :
            
            size = len(queue)
            for _ in range(size):
                row,col = queue.popleft()
                if (row,col) in visited:
                    continue
                visited.add((row,col))
                values[(row,col)] = level
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if self.isValid(nr,nc,grid):
                        queue.append((nr,nc))
            level += 1
        heap = [(-1*values[(0,0)],0,0)]
        visited = set()
        while heap:
            dis,row,col = heapq.heappop(heap)
            if (row,col) in visited:
                continue
            visited.add((row,col))
            if (row,col) == (len(grid)-1,len(grid)-1):
                return -1*dis
            
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                
                if self.isValid(nr,nc,grid):
                    heapq.heappush(heap,(-1*min(-1*dis,values[(nr,nc)]),nr,nc))
        
                
        