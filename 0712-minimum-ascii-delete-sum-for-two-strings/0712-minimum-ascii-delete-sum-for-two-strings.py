class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @cache
        def dp(index1,index2):
            
            if index1 == len(s1) or index2 == len(s2):
                min_cost = 0
                for i in range(index1,len(s1)):
                    min_cost += ord(s1[i])
                for i in range(index2,len(s2)):
                    min_cost += ord(s2[i])
                
                return min_cost
            
            if s1[index1] == s2[index2]:
                return dp(index1+1,index2+1)
            
            return min(ord(s1[index1])+dp(index1+1,index2),ord(s2[index2])+dp(index1,index2+1))
        
        return dp(0,0)
                