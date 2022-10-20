class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        dp = defaultdict(lambda:[0,0])
        max_area = 0
        for row in range(len(matrix)-1,-1,-1):
            depth = {}
            for col in range(len(matrix[0])-1,-1,-1):
                if matrix[row][col]=="1":
                    
                    dp[(row,col)][0]=1+dp[(row,col+1)][0]
                    dp[(row,col)][1]=1+dp[(row+1,col)][1]
                    
                    if dp[(row,col)][1] not in depth: 
                        depth[dp[(row,col)][1]] = col + 1
                    deleted = []
                    for key in depth.keys():
                        if key > dp[(row,col)][1]:
                            depth[dp[(row,col)][1]] = max(depth[key],depth[dp[(row,col)][1]])
                            deleted.append(key)
                    for key in deleted:
                        del depth[key]
                            
                            
                    
                        
                    for dep in depth.keys():
                        
                        max_area = max(dep*(depth[dep]-col),max_area)
                    
                else:
                    
                    depth = {}
        return max_area
                