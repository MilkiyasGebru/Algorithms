class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        arr = [0 for _ in range(n)]
        self.answer = 0
        
        def backTrack(index,count):
            

            if count + len(requests) - index <= self.answer :
                return
            
            if  max(arr) == min(arr) and max(arr) == 0 :
                
                self.answer = max(self.answer, count)
            
            if index == len(requests)   :
                    
                
                return 
            
            for i in range(index,len(requests)):
                
                    
                arr[requests[i][0]] -= 1
                arr[requests[i][1]] += 1
                
                
                backTrack(i+1,count+1)
                

                arr[requests[i][0]] += 1
                arr[requests[i][1]] -= 1
        
        
        backTrack(0,0)
        return self.answer
                
        
        