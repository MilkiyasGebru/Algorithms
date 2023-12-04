class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        curr = capacity
        total_steps = 0
        
        for i in range(len(plants)):
            total_steps += 1
            if curr >= plants[i]:
                curr -= plants[i]
            
            else:
                total_steps += (i)*2
                curr = capacity - plants[i]
            
        return total_steps  