class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        letters =[a,b,c]
        heap = []
        string = []
        for i in range(3):
            if letters[i] > 0:
                heapq.heappush(heap,(-letters[i],97 + i))
        prev_letter,prev_count= "",0
        while heap:
            
            total,letter = heapq.heappop(heap)
            
            if letter == prev_letter and prev_count == 2:
                
                if heap:
                    
                    next_total,next_letter = heapq.heappop(heap)
                    string.append(chr(next_letter))
                    prev_letter,prev_count = next_letter,1
                    
                    if next_total + 1:
                        heapq.heappush(heap,(next_total+1,next_letter))
                        
                    heapq.heappush(heap,(total,letter))
                else:
                    
                    break
            else:
                
                string.append(chr(letter))
                prev_count = prev_count + 1 if letter == prev_letter else 1
                prev_letter = letter
                
                if total + 1:
                    heapq.heappush(heap,(total+1,letter))
                    
        return "".join(string)
        