class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def rec(i,m):
            
            if i >= len(piles):
                return 0
            
            z,s=-inf,0
            
            for index in range(i,min(i+2*m,len(piles))):
                
                s += piles[index]
                z=max(z,s-rec(index+1,max(index-i+1,m)))
               
            return z    
        
        return (rec(0,1)+sum(piles))//2