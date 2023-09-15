class UnionFind:
    
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def findParent(self,point):
        
        if self.parent[point] == point:
            return point
        parentPoint = self.findParent(self.parent[point])
        self.parent[point] = parentPoint
        return parentPoint
    
    def unionParent(self,x,y):
        
        par1 = self.findParent(x)
        par2 = self.findParent(y)
        
        if par1 == par2:
            return False
        
        if self.rank[par1] < self.rank[par2]:
            par1,par2 = par2,par1
        
        self.rank[par1] += self.rank[par2]
        self.parent[par2] = par1
            
        
        return True

class Solution:
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = []
        minCost = 0
        
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                heappush(edges,(abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]),i,j))
                
        graph = UnionFind(len(points))
        
        while edges:
            
            weight,x,y = heappop(edges)
            if graph.unionParent(x,y):
                minCost += weight
                
        return minCost
            
            