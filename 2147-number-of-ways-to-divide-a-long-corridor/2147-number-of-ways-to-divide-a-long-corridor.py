class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        self.mod = 10**9 + 7
        cache = [[-1 for _ in range(3)] for _ in range(len(corridor))]
        
        def dp(index,count):
            
            if index == len(corridor):
                return 1 if count == 2 else 0
            
            if cache[index][count] != -1:
                return cache[index][count]
            
            if corridor[index] == "S":
                
                if count == 2:
                    cache[index][count] = dp(index+1,1)%self.mod
                    
                else:
                    cache[index][count] = dp(index+1,count+1)%self.mod
            
            else:
                
                if count == 2:
                    cache[index][count] = (dp(index+1,count) + dp(index+1,0))%self.mod
                    
                else:
                    cache[index][count] = dp(index+1,count)%self.mod
                    
            return cache[index][count]
            
        return dp(0,0)
                    