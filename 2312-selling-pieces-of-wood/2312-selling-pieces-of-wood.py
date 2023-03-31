class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        f = defaultdict(int)
        for h,w,p in prices:
            f[(h,w)] = p
        
        @lru_cache(None)
        def findMax(n,m):
            
            ans = f[(n,m)]
            
            # horizontal cut
            for i in range(1,n):
                ans = max(ans,  findMax(i,m) + findMax(n-i,m) )
            
            # vertical cut
            for i in range(1,m):
                ans = max(ans,  findMax(n,i) + findMax(n,m-i))
            
            return ans
        
        return findMax(m,n)