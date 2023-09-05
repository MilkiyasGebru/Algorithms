class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        visited = set()
        def addtoSet():
            for i in range(1,k+1):
                visited.add(i)
        addtoSet()
        count = 1
        for i in range(len(rolls)-1,-1,-1):
            
            if rolls[i] in visited:
                visited.remove(rolls[i])
            
            if len(visited) == 0:
                count += 1
                addtoSet()
        
        return count 
        