class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        
        visited = set()
        
        count = 1
        
        for i in range(len(rolls)):
            
            visited.add(rolls[i])
            
            if len(visited) == k:
                
                visited = set()
                count += 1    
            
            
        return count 
        