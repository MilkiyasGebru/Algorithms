class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        time = 0
        new_array = []
        
        for i in range(len(plantTime)):
            new_array.append((growTime[i],plantTime[i]))
        
        new_array.sort(reverse=True)
        
        answer = 0
        
        for i in range(len(new_array)):
            
            time += new_array[i][1]
            answer = max(answer,time + new_array[i][0])
        
        return answer
            
            
        