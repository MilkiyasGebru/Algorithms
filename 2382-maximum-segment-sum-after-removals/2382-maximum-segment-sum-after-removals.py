class UnionFind:
    
    def __init__(self,nums):
        
        self.rank = nums
        self.parent = [i for i in range(len(nums))]
    
    def findParent(self,node):
        
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self,node1,node2):
        
        par1 = self.findParent(node1)
        par2 = self.findParent(node2)
        
        if par1 == par2:
            return
        
        if self.rank[par1]  < self.rank[par2]:
            par1,par2 = par2,par1
        
        self.rank[par1] += self.rank[par2]
        self.parent[par2] = par1
        return 
    def get(self,node):
        return self.rank[self.findParent(node)]
    
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        
        answer = [0 for i in range(len(nums)+1)]
        graph = UnionFind(nums)
        visited = set()
        max_segment = 0
        for i in range(len(nums)-1,-1,-1):
            
            index = removeQueries[i]
            if index + 1 in visited:
                
                graph.union(index,index+1)
            if index - 1 in visited:
                graph.union(index,index-1)
                
            visited.add(index)
            max_segment = max(max_segment,graph.get(index))
            answer[i] = max_segment
            
        return answer[1:]