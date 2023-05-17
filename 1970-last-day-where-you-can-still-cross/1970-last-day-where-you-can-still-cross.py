class UnionFind:
    
    def __init__(self,row,col):
        self.parent = [[0 for _ in range(col+2)] for _ in range(row+2) ]
        self.rank = [[1 for _ in range(col+2)] for _ in range(row+2)]
        
        for i in range(len(self.parent)):
            
            self.parent[i][0] = "L"
            self.parent[i][-1] = "R"
            self.rank[i][0] = self.rank[i][-1] = float("inf")
        
    
    def findParent(self,row,col):
        
        if self.parent[row][col] in {"L","R",(row,col),0}:
            return self.parent[row][col]
        
        r,c = self.parent[row][col]
        self.parent[row][col] = self.findParent(r,c)
        return self.parent[row][col]
    
    def union(self,row,col):
        
        self.parent[row][col] = (row,col)
        directions = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        boolean = False
        
        for i,j in directions:
            boolean = boolean or self.Callunion(row,col,row+i,col+j)
            
        return boolean
    
    def Callunion(self,row,col,new_row,new_col):
        par1 = self.findParent(row,col)
        par2 = self.findParent(new_row,new_col)
        
        if par1 == par2 or par2 == 0:
            return False
        
        if par1 in {"L","R"} and par2 in {"L","R"}:
            return True
        
        if par1 in {"L","R"} or par2 in {"L","R"}:
            if par2 in {"L","R"}:
                par1,par2 = par2,par1
            self.parent[par2[0]][par2[1]] = par1
            return 
                
        
        if self.rank[par2[0]][par2[1]] > self.rank[par1[0]][par1[1]]:
            par1,par2 = par2,par1
        
        self.parent[par2[0]][par2[1]] = par1
        self.rank[par1[0]][par1[1]] += self.rank[par2[0]][par2[1]]
        return False
        

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        last_day = 0
        matrix = UnionFind(row,col)
        
        for day in range(len(cells)):
            
            if matrix.union(cells[day][0],cells[day][1]):
                
                return day
        