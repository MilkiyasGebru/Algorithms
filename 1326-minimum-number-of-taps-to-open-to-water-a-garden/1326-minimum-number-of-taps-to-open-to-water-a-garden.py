class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        arr = []
        
        for i in range(len(ranges)):
            
            arr.append((max(0,i-ranges[i]),min(len(ranges)-1,i+ranges[i])))
        
        arr.sort(key = lambda x: x[0])
        last = 0
        tapsNeeded = 0
        
        i = 0
        while i < len(arr) and last < len(ranges)-1:
            
            temp = last
            
            while i < len(arr) and arr[i][0] <= last :
                temp = max(arr[i][1],temp)
                i+=1
                
            if last == temp:
                return -1
            
            last = temp
            tapsNeeded += 1 
       
        return tapsNeeded 
            
            
            
            
        
        
            
        
        
        
        