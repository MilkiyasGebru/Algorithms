class UnionFind:
    
    def __init__(self,n):
        self.rank = [0 for _ in range(n)]
        self.parent = [i for i in range(n)]
    
    def findParent(self,n):
        if n == self.parent[n]:
            return n
        self.parent[n] = self.findParent(self.parent[n])
        return self.parent[n]
    
    def union(self,u,v):
        par1 = self.findParent(u)
        par2 = self.findParent(v)
        
        if par1 == par2:
            return
        if self.rank[par2] > self.rank[par1]:
            par1,par2 = par2,par1
        self.rank[par1]+=self.rank[par2]
        self.parent[par2]=par1
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        min_num = min(nums)  
        max_num = max(nums)
        set_nums = set(nums)
        graph = UnionFind(max_num+1)
        for fact in range(2,(max_num+2)//2):
            num = fact
            while num <= max_num:
                if num in set_nums:
                    graph.union(num,fact)
                num += fact
        
        
        for i in range(1,len(nums)):
            if graph.findParent(nums[i]) != graph.findParent(nums[i-1]):
                return False
        
        
        return min_num != 1 or len(nums) == 1
            
                
            