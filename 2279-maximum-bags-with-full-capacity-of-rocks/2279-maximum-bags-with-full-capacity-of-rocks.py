class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        new_array = []
        for i in range(len(capacity)):
            new_array.append(capacity[i]-rocks[i])
        new_array.sort()
        answer = i = 0
        while i < len(capacity) and additionalRocks >= 0:
            
            additionalRocks -= new_array[i]
            answer += 1
            i += 1
        
        return answer if additionalRocks >= 0 else answer - 1
        