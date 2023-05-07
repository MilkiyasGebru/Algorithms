class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        
        prefix = [0 for _ in range(len(floor) + 1)]
        
        for i in range(len(floor)-1,-1,-1):
            prefix[i] = prefix[i+1] + 1*(floor[i] == "1")
        
        @lru_cache(None)
        def dp(index,numCarpets):
            
            if index >= len(floor):
                return 0
            
            if numCarpets == 0:
                
                return prefix[index]
            
            if floor[index] == "0":
                return dp(index+1,numCarpets)
            
            return min( 1 + dp(index+1,numCarpets), dp(index+carpetLen,numCarpets-1))
        
        
        return dp(0,numCarpets)