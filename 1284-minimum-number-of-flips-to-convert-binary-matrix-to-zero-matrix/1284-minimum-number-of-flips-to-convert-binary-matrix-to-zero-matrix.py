class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        
        mask = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        def isValid(row,col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]:
                    curr = (row)*len(mat[0]) + (col)
                    mask |= 1 << curr
        visited = set()
        queue = deque([mask])
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                
                mask = queue.popleft()
                if mask in visited:
                    continue
                if mask == 0:
                    return steps
                visited.add(mask)
                
                for i in range(len(mat)):
                    for j in range(len(mat[0])):
                        curr = (i)*len(mat[0]) + j 
                        mask ^= 1 << curr
                        for dx,dy in directions:
                            if isValid(i+dx,j+dy):
                                curr = (i+dx)*len(mat[0]) + j  + dy
                                mask ^= 1 << curr
                        
                        queue.append(mask)
                        curr = (i)*len(mat[0]) + j 
                        mask ^= 1 << curr
                        for dx,dy in directions:
                            if isValid(i+dx,j+dy):
                                curr = (i+dx)*len(mat[0]) + j  + dy
                                mask ^= 1 << curr
            steps += 1
        return -1
                
                