class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        heap = []
        answer = []
        
        for index in range(len(tasks)):
            tasks[index].append(index)
        
        tasks.sort()
        time = tasks[0][0]
        
        i = 0
        
        while( i < len(tasks) or heap):
            
            if len(heap) == 0:
                time = max(time, tasks[i][0])
                
            while( i < len(tasks) and time >= tasks[i][0]):
                
                heapq.heappush(heap,(tasks[i][1],tasks[i][2]))
                
                i+=1
                
            
            a,b = heapq.heappop(heap)
                
            time += a 
            answer.append(b)
                
        
        
        return answer
            
            
        
        