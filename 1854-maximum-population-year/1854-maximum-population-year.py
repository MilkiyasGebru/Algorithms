class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        answer = 1950
        
        
        prefix = [ 0 for i in range(101) ] 
        
        for birth,death in logs:
            
            prefix[birth - 1950] += 1
            prefix[death - 1950] -= 1
            
        max_population = prefix[0]
        
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
            if prefix[i] > max_population:
                answer = i + 1950
                max_population = prefix[i]
        
        return answer