class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        
        @lru_cache(None)
        def dp(index,numCarpets):
            
            if index >= len(floor):
                return 0
            
            if numCarpets == 0:
                
                return floor[index:].count("1")
            
            return min( 1*(floor[index]=="1") + dp(index+1,numCarpets) , dp(index+carpetLen,numCarpets-1))
        
        return dp(0,numCarpets)